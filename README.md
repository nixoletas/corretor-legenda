Esse srcipt corrige legendas bugadas.

Ex:
```
2
00:00:03,020 --> 00:00:05,440
<font face="Trebuchet MS"><font size="24"><i>Ã‰ um sinal de que o conto chegou ao fim</i></font></font>

3
00:00:05,440 --> 00:00:08,360
<font face="Trebuchet MS"><font size="24"><i>Como uma Ãºnica passagem tirada</i></font></font>
```

saída: 
```
2
00:00:03,020 --> 00:00:05,440
<font face="Trebuchet MS"><font size="24"><i>É um sinal de que o conto chegou ao fim</i></font></font>

3
00:00:05,440 --> 00:00:08,360
<font face="Trebuchet MS"><font size="24"><i>Como uma única passagem tirada</i></font></font>
```

```bash
python app.py
```
