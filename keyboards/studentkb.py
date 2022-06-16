from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

##################row insert #######################################

kb_korpusa = InlineKeyboardMarkup(row_width=4).row(InlineKeyboardButton(text='Главный корпус',callback_data='korp_gk')).row(InlineKeyboardButton(text='Корпус №1',callback_data='korp_1'))


urlkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Карта',url='https://yandex.ru/maps/?um=constructor%3Acaf5ec63cae8f20d89ee6b2c9de5ccab5ae4cce9e77bc7cc586dc40be983bc56&source=constructorLink'))

kb_ucheba=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Личный кабинет',callback_data='lk'))\
    .add(InlineKeyboardButton(text='Глоссарий',callback_data='glos')).add(InlineKeyboardButton(text='Твой Политех',callback_data='tpu'))\
    .add(InlineKeyboardButton(text='Стипендия',callback_data='cash'))


kb_tvor4 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Творчество',callback_data='tvor4'))\
    .add(InlineKeyboardButton(text='Спорт',callback_data='sport'))

kb_student= InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Студенческая жизнь в ТПУ',callback_data='culture'))\
                                            .add(InlineKeyboardButton(text='Учебный процесс',callback_data='ucheba'))\
                                            .add(InlineKeyboardButton(text='Навигация в кампусе',callback_data='gps'))\
                                            .add(InlineKeyboardButton(text='Навигация в корпусах',callback_data='nav'))

