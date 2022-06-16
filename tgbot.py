from create_tgbot import dp
from aiogram.utils import executor





from handlers import student

student.register_handlers_student(dp)


executor.start_polling(dp,skip_updates=True)