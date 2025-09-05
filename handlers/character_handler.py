from services import CharacterService, InventoryService
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import (character_keyboard, add_scores_keyboard, NewScores, CharacterCallback, AddScoresCallback)
from repositories import Character
from keyboards import inventory_keyboard


class CharacterHandler:
    def __init__(
        self, 
        character_service: CharacterService,
        inventory_service: InventoryService
    ):
        self.character_service = character_service
        self.inventory_service = inventory_service

    async def character_handler(self, msg: types.Message):
        character = self.character_service.get_by_user_id(msg.from_user.id)
        await msg.answer_photo(
            photo=types.FSInputFile("images/Character_menu.jpg"), 
            caption=f"Данные о герое:\nУровень: {character.level}\nОпыт до следующего уровня: {character.experience}\nБаланс: {character.balance}\nСила: {character.streight}\nТелосложение: {character.physique}\nЛовкость: {character.agility}", 
            reply_markup=character_keyboard(character.available_scores)
        )

    async def character_menu_handler(
            self, callback: types.CallbackQuery, callback_data: CharacterCallback, state: FSMContext
    ):
        if callback_data.action == "score_up":
            character = self.character_service.get_by_user_id(callback.from_user.id)
            scores = NewScores()
            await state.update_data(scores=scores, character=character)
            await callback.message.edit_caption(
                text="Распределите характеристики", 
                reply_markup=add_scores_keyboard(character, scores)
            )
        elif callback_data.action == "inventory":
            character = self.character_service.get_by_user_id(callback.from_user.id)
            inventory = self.inventory_service.get_inventory(character.id)
            await callback.message.edit_caption(
                text="Инвентарь",
                reply_markup=inventory_keyboard(inventory)
            )
    
    async def score_up_handler(self, callback: types.CallbackQuery, callback_data: AddScoresCallback, state: FSMContext):
        data = await state.get_data()
        character: Character = data.get("character")
        scores: NewScores = data.get("scores")

        is_changed = False

        if callback_data.action == "inc":
            if character.available_scores > 0:
                character.available_scores -= 1
                is_changed = True
                match callback_data.feature:
                    case "streight":
                        scores.streight += 1
                    case "agility":
                        scores.agility += 1
                    case "physique":
                        scores.physique += 1
            else:
                await callback.answer("Свободных очков больше нет")
        elif callback_data.action == "dec":
            match callback_data.feature:
                case "streight":
                    if scores.streight > 0:
                        scores.streight -= 1
                        character.available_scores += 1
                        is_changed = True
                    else:
                        await callback.answer("Нельзя больше уменьшить")
                case "agility":
                    if scores.agility > 0:
                        scores.agility -= 1
                        character.available_scores += 1
                        is_changed = True
                    else:
                        await callback.answer("Нельзя больше уменьшить")
                case "physique":
                    if scores.physique > 0:
                        scores.physique -= 1
                        character.available_scores += 1
                        is_changed = True
                    else:
                        await callback.answer("Нельзя больше уменьшить")
        elif callback_data.action == "done":
            self.character_service.update_scores(character, scores)
            await callback.message.edit_caption(text="Вы хорошо прокачались, ваши характеристики изменены!")
        
        if is_changed and callback_data.action in ("inc", "dec"):
            await state.update_data(character=character, scores=scores)
            await callback.message.edit_reply_markup(
                reply_markup=add_scores_keyboard(character, scores)
            )
        


