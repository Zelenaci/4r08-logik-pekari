# PRG --  Logik

[![Join the chat at gitter.im/spseol/Python](https://badges.gitter.im/spseol/PRG-No.svg)](https://gitter.im/spseol/Python?utm_source=share-link&utm_medium=link&utm_campaign=share-link)


## Popis porgramu

Jde o počítačovou verzi staré známé deskové hry Logik. 

Pro lepší zážitek hra obsahuje i vestavěný jukebox, který hraje na základě toho, zda hráč vyhrál, nebo prohrál. Výchozí playlist je sestaven převážně z osmdesátkových hitovek, což je doba, kdy tato hra nejvíc letěla. Najde se zde však i pár novějších kousků, protože i dnes je Logik stále známý pojem. 

Jednotlivé skladby jsou vybírány náhodně. Asi nikdo nemá rád, když se hraje jedna písnička stále dokola, což by se při náhodném výběru mohlo stát. Ostatně, komu se nestalo, že mu při člověče nezlob se padla 8x po sobě třeba šestka… V případě šestky při člověče nezlob se je to jistě příjemná skutečnost. Mnohem méně příjemné by však bylo, poslouchat 8x po sobě stejnou písničku. To se vám s tímto jukeboxem nestane. Dokud jukebox nevyčerpá všechny skladby z playlistu, nebo nedojde k restartování hry, žádná skladba nezahraje více, než jednou.

Playlist už v základu obsahuje velká jména, jako Bee Gees, Ozzy Osbourne, Journey a mnoho dalších. Komu by to nestačilo, není nic jednoduššího, než otevřít jeden z textových souborů ve složce jukebox a přidat své písničky.

Příjemnou zábavu vám přejí autoři:
* <b>Kryshi</b> – hlavní designér, PDF (programátor doplňujících funkcí)
* <b>Váša</b> – programátor, juke box hero

## Zadání

Implementujte deskovou hru Logik. Hracím kamenům budou odpovídat barvy.

Máme k dispozici
 * 8 druhů hracích kamemů
 * 2 druhy vyhodnocovacích kamenů -- tato informace lze sdělit i textově takže
   je nemusíte používat

Na začátku hry je náhodně rozmístěno 5 různých hracích kamenů. Druh hracího
kamenu se nesmí opakovat. Hráč hádá rozmístění kamenů.

Program při každém pokusu hráči sdělí:

 1. kolik kamenů je použito správně, co do druhu i pozice 
   (černé vyhodnocovací kameny)
 2. kolik kamenů je správného druhu, ale na nesprávné pozici (bílé 
    vyhodnocovací kameny) Toto sdělení může být číslovkou nebo pomocí
    vyhodnocovacího kamene

Hráč má 10 pokusů na to, aby uhodl skrytou kombinaci. Po uhodnutí nebo po
vyčerpání všech pokusů program ukáže zadanou kombinaci.

![logik.png](logik.png)



* <https://mamut.spseol.cz/nozka/python/priklad_logik/>
