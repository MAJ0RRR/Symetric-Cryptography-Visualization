# Projekt na Przedmiot "Wprowadzenie do Cyberbezpieczeńśtwa"

# Temat 14 
Implementacja aplikacji szyfrującej i deszyfrującej pliki z wykorzystaniem kryptografii symetrycznej.

# Instrukcja uruchomienia
Wszystkie pliki należy umieścić w folderze, a następnie uruchomić skrypt inicjalizayjny poleceniem './setup.py' , który zainstaluje wszystkie potrzebne
dependencje zawarte w pliku 'requirements.txt'
Następnie polecenie './main.py' uruchamia aplikację w trybie graficznym.

# Działanie
Aplikacja potrafi szyfrować i deszyforwać pliki w kilku trybach (ECB,CBC,CTR).
Aby rozpocząć pracę należy wybrać akcję,tryb oraz interesujący nas tryb i kliknąć 'run'.Pliki pozwalające na sensowny ich podgląd będą wyświetlane w miejscu
okienek ze znakami zapytania.
W celach dydaktycznych jest możliwość ustawienia poziomu błędu w szyfrogramie w procentach zarówno podczas szyforwania jak i deszyforwania.

# Output
Po szyfrowaniu w folderze data tworzony jest plik z rozszerzeniem '.secret'.
Natomiast podczas każdej akcji tworzone są odpowiednio pliki odszyforwane z infixem '-dec' i zaszyfrowane '-enc'.
W przypadku symulowania błędu tworzony jest plik z infixem '-err', który przedstawia, któe bajty zostały losowo przekłamane.

# ECB

# CBC 

# CTR
