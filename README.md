Якунчева Ирина Юрьевна, группа 166, Проект Персональный медицинский помощник

Описание:
Медицинские приложения стали очень широко используемы в практике Профессионального Здравоохранения, и со временем, планируется их широкое внедрение во все отрасли клинической практики. Есть много преимуществ которые дают медицинские приложения и устройства, однако они в настоящее время используются без полного понимания связанных с ними рисков и преимуществ. Поэтому, чтобы обеспечить высокий уровень качества и безопасности при использовании данных интсрументов, требуется точная оценка и разработка лучших стандартов. Ключевым моментом в достижении этой цели служит способность приложения давать значимую, точную и своевременную информацию для пользователя о тех или иных данных.

На сегодняший день существует множество решений для реализации медицинских ассистентов. Они направены на сбор и анализ данных в зависимости от напревления медицины. Например, програмные обесечения производимые AMPS(Analyzing Medical Parameters for Solutions) являются мощными инструментами в количественном анализе ЭКг и мониторинге артериального давления. Другой пример програмного инструмента от ECGsoft- это приложение EcgViewer, которое является одновременно автономным 12-канальным средством просмотра ЭКГ предоставляющим графический интерфейс для отображения, просмотра и редактирования ЭКГ. Пользователь может также реализовать свой собственный формат данных, используя предоставленный открытый интерфейс. C # ECG Toolkit - также программный инструментарий для преобразования, просмотра и печати электрокардиограмм. Инструментарий разработан с использованием C # .NET 2.0 (код также поддерживает 1.1, 3.5 и 4.0). Siera Ecg Tools предназначен только для форматов Philips Sierra ECG XML.

### Запуск приложения на компьюетере
Для запуска на Ubuntu 16.04 требуется выполнить следующие шаги:
1) Установить python:
```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```
2) Установить kivy:
```
sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get update
sudo apt-get install python-kivy
```
3) Установить KivyCalendar
```
sudo pip install KivyCalendar
```
4) Установить pymongo
```
sudo python -m pip install pymongo
```
Теперь можно запускать приложение
```
python main.py
```
