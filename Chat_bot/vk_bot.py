import requests
import bs4
import currency_converter


class VkBot:

    def __init__(self, user_id):
        print("Создан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["ПРИВЕТ", "ПОКА", "КОНВЕРТ", "КУРС", "HELP", "НАЧАТЬ"]
        self.help = "Вас приветствует финансовый бот-помощник.\n" \
                    "Если вам нужно конвертировать валюту - напишите Конвертация, дальше напишите валюту," \
                    " которую хотите обменять, потом количество валюты и название валюты, В которую хотите обменять.\n" \
                    "Например: USD 120 RUB\n" \
                    "Если хотите посмортеть сокращения большинства валют - напиштите Валюты"
        self.val = "AUD  -	Австралийский доллар\n AZN  -	Азербайджанский манат\nAMD  -	Армянских драмов\n" \
                   "BYN  -	Белорусский рубль\nBGN  -	Болгарский лев\nBRL  -	Бразильский реал\nHUF  -	Венгерских форинтов\n" \
                   "KRW  -	Вон Республики Корея\nHKD  -	Гонконгских долларов\nDKK  -	Датская крона\nUSD  -	Доллар США\n" \
                   "EUR  -	Евро\nINR  -	Индийских рупий\nKZT  -	Казахстанских тенге\nCAD  -	Канадский доллар\nKGS  -	Киргизских сомов\n" \
                   "CNY  -	Китайский юань\nMDL  -	Молдавских леев\nTMT  -	Новый туркменский манат\nNOK  -	Норвежских крон\n" \
                   "PLN  -	Польский злотый\nRON  -	Румынский лей\nXDR  -	СДР\nSGD  -	Сингапурский доллар\nTJS  -	Таджикских сомони\n" \
                   "TRY  -	Турецких лир\nUZS  -	Узбекских сумов\nUAH  -	Украинских гривен\nGBP  -	Фунт стерлингов Соединенного королевства\n" \
                   "CZK  -	Чешских крон\nSEK  -	Шведских крон\nCHF  -	Швейцарский франк\nZAR  -	Южноафриканских рэндов\n" \
                   "JPY  -	Японских иен"

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):

        # Привет
        if self._COMMANDS[0] in message.upper() or self._COMMANDS[5] in message.upper():
            return f"Привет-привет, {self._USERNAME}! Если нужна помощь, напиши: <<help>>"

        # Пока
        elif self._COMMANDS[1] in message.upper():
            return f"Пока-пока, {self._USERNAME}!"
        elif self._COMMANDS[2] in message.upper() or self._COMMANDS[3] in message.upper():
            return "конвертер"
        elif self._COMMANDS[4] in message.upper():
            return self.help
        elif "ВАЛЮТ" in message.upper():
            return self.val

        else:
            return "Не понимаю о чем вы..."

    # Метод для очистки от ненужных тэгов

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

