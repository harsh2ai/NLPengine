### Insult Detection Model
1. Using deeppavlov api :Insult detection predicts whether a comment posted during a public discussion is considered insulting to one of the participants. This component is the defense against spam and abuse in your business.

```
Sample Output:
{'insult_detection':[{'?RT @justinbiebcr: The bigger the better..shit....if you know what I mean ;)': {'Not Insult'}},
                    {"if my mom went on for the love of ray J or any reality show i'd bee pissed .": {'Not Insult'}},
                    {"@BarCough it's enough to make you sick, eh? there's nothing sacred anymore": {'Not Insult'}},
                    {'Hacienda is now level 80 time to get epic gear for her!!!! Oh and maybe some sleep would be good..': {'Not Insult'}}, 
                    {'"Iran, with its unity and God\'s grace, will punch the arrogance (West) 22nd of Bahman (Feb 11) in a way that will leave them stunned,"': {'Not Insult'}}, 
                    {'@russmarshalek Sold! Would love to be your crazyass big sis -- how could I say no?! Cannot believe I broke or minimally battered my toe --': {'Not Insult'}}, 
                    {'You are such an idiot and dumbass.':{'Insult'},
                    {'i need money! i need new car!!! jesus...somebody please buy my old car :DDD': {'Not Insult'}}]}

```

