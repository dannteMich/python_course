<div dir="rtl">

# כלים שונים לבדיקות תנאים

## השוואת עבור מספרים

סימן/שם | מה זה עושה | דוגמא
--- | --- | ---
| <, > | קטן מ... גדול מ... | 10 > 102 |
| <=, >=  | קטן או שווה.... גדול או שווה... | 12 >= 12 |
| == | שווין - בודק האם שני הצדדים שווים. שימו לב לסימון הכפול | 3.12 == 3.00
| =! | שוני - בודק ששני המספרים **אינם** שווים זה לזה | 3 =! 4

## עבור מחרוזות

 **in** - בדיקת תת מחרוזת - מאפשר לבדוק אם מחרוזת אחת נמצאת בתוך אחרת

<div dir="ltr">

```python
'a' in 'hello world'    # Flase
'w' in 'hello world'    # True
'wor' in 'hello world'  # True
'WOr' in 'hello world'  # False
```
</div>

</div>