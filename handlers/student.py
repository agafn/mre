from create_tgbot import dp, bot
from aiogram import types, Dispatcher
from keyboards import kb_student, kb_tvor4,kb_ucheba, urlkb,kb_korpusa
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

class number(StatesGroup):
    number_of_korpus = State()
    number_audit = State()



#@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    await message.answer(f'Привет!\n'
                        'Я - твой личный помощник.\n'
                        'И я помогу тебе в твоей адаптации.\n',reply_markup=kb_student)
    await message.delete()


@dp.callback_query_handler(text='culture')
async def culture_call(callback: types.CallbackQuery):
    await callback.message.answer('Студенчество – это не только учеба.\n'
                         ' ТПУ создает безграничные возможности для активной, творческой жизни студентов!',reply_markup=kb_tvor4)

@dp.callback_query_handler(text='ucheba')
async def ucheba_call(callback: types.CallbackQuery):
    await callback.message.answer('Что именно интересует?',reply_markup=kb_ucheba)


@dp.callback_query_handler(text='gps')
async def gps_call(callback: types.CallbackQuery):
    await callback.message.answer('Карта кампуса по кнопке ниже',reply_markup=urlkb)



@dp.callback_query_handler(text='nav', state=None)
async def nav_call(callback:types.CallbackQuery):
    await number.number_of_korpus.set()
    await callback.message.answer('Выберите корпус',reply_markup=kb_korpusa)


@dp.callback_query_handler(content_types='text', state=number.number_of_korpus)
async def audit_(callback:types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['number_of_korpus']==callback.message.text
    await number.next()
    await callback.message.answer('С помощью клавиатуры введите номер аудитории')


@dp.message_handler(state=number.number_audit)
async def naviga(message: types.Message, state: FSMContext):
    if message.text==Text(startswith='1'):
        await bot.send_photo(message.chat.id, photo="D:/tg_assistant\Карта корпусов\ГК/1 этаж.png")


def register_handlers_student(dp: Dispatcher):
    dp.register_message_handler(command_start,commands=['start','help'])

