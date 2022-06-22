# Spectorial

Instant access in the terminal to the D&D 5e knowledgebase using the [RESTful API](https://www.dnd5eapi.co/).

* A Candlekeep monk will retrieve for you the information you are looking for. So no need to interact with the code.
* Said monk is very efficient, therefore the app is also suitable to search things on-the-fly during sessions.
* See the screenshots to look at how the requests are carried out.

## Using Spectorial

Clone the repository. Run `spectorial.sh` to execute Spectorial. Done.

```
git clone https://github.com/alussana/spectorial
cd spectorial
bash spectorial.sh
```

The information is readily retrieved and displayed with a minimal amount of input. Here a couple of examples:

### Initialization and browsing cathegories

```
 Candlekeep Monk:
 "Greetings. Just one moment and I'll help you with your quest."
 *Opens a tome and summons the Internet planar portal*

 Candlekeep Monk:
 "Here we are. What kind of knowledge are you looking for?"

{0: 'ability-scores',
 1: 'alignments',
 2: 'backgrounds',
 3: 'classes',
 4: 'conditions',
 5: 'damage-types',
 6: 'equipment',
 7: 'equipment-categories',
 8: 'feats',
 9: 'features',
 10: 'languages',
 11: 'levels',
 12: 'magic-items',
 13: 'magic-schools',
 14: 'monsters',
 15: 'proficiencies',
 16: 'races',
 17: 'rule-sections',
 18: 'rules',
 19: 'skills',
 20: 'spells',
 21: 'subclasses',
 22: 'subraces',
 23: 'traits',
 24: 'weapon-properties'}

 --> : 3

 Candlekeep Monk:
 "Very well, classes. Here is what I have."

{0: 'Barbarian',
 1: 'Bard',
 2: 'Cleric',
 3: 'Druid',
 4: 'Fighter',
 5: 'Monk',
 6: 'Paladin',
 7: 'Ranger',
 8: 'Rogue',
 9: 'Sorcerer',
 10: 'Warlock',
 11: 'Wizard'}

 --> :
```

### Searching and displaying Magic Missile

```
 Candlekeep Monk:
 "How may I assist you?"

{0: 'ability-scores',
 1: 'alignments',
 2: 'backgrounds',
 3: 'classes',
 4: 'conditions',
 5: 'damage-types',
 6: 'equipment',
 7: 'equipment-categories',
 8: 'feats',
 9: 'features',
 10: 'languages',
 11: 'levels',
 12: 'magic-items',
 13: 'magic-schools',
 14: 'monsters',
 15: 'proficiencies',
 16: 'races',
 17: 'rule-sections',
 18: 'rules',
 19: 'skills',
 20: 'spells',
 21: 'subclasses',
 22: 'subraces',
 23: 'traits',
 24: 'weapon-properties'}

 --> : 20

 Candlekeep Monk:
 "Let me see... I've got 319 results for spells.
 Do you know its name already? If not, try to use the first letters only."

 --> : Mag

{185: 'Mage Armor',
 186: 'Mage Hand',
 187: 'Magic Circle',
 188: 'Magic Jar',
 189: 'Magic Missile',
 190: 'Magic Mouth',
 191: 'Magic Weapon',
 192: 'Magnificent Mansion'}

 --> : 189

 Candlekeep Monk:
 "Here is what you asked for. Use it wisely."

     _______________________________________________________________________________________
    /\                                                                                      \
(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
    \/______________________________________________________________________________________/

      {'_id': '62b248818b12b6a08c9fa6c1',
       'casting_time': '1 action',
       'classes': [{'index': 'sorcerer',
                    'name': 'Sorcerer',
                    'url': '/api/classes/sorcerer'},
                   {'index': 'wizard',
                    'name': 'Wizard',
                    'url': '/api/classes/wizard'}],
       'components': ['V', 'S'],
       'concentration': False,
       'damage': {'damage_at_slot_level': {'1': '1d4 + 1',
                                           '2': '1d4 + 1',
                                           '3': '1d4 + 1',
                                           '4': '1d4 + 1',
                                           '5': '1d4 + 1',
                                           '6': '1d4 + 1',
                                           '7': '1d4 + 1',
                                           '8': '1d4 + 1',
                                           '9': '1d4 + 1'},
                  'damage_type': {'index': 'force',
                                  'name': 'Force',
                                  'url': '/api/damage-types/force'}},
       'desc': ['You create three glowing darts of magical force. Each dart hits a '
                'creature of your choice that you can see within range. A dart deals '
                '1d4 + 1 force damage to its target. The darts all strike '
                'simultaneously, and you can direct them to hit one creature or '
                'several.'],
       'duration': 'Instantaneous',
       'higher_level': ['When you cast this spell using a spell slot of 2nd level or '
                        'higher, the spell creates one more dart for each slot level '
                        'above 1st.'],
       'index': 'magic-missile',
       'level': 1,
       'name': 'Magic Missile',
       'range': '120 feet',
       'ritual': False,
       'school': {'index': 'evocation',
                  'name': 'Evocation',
                  'url': '/api/magic-schools/evocation'},
       'subclasses': [{'index': 'lore',
                       'name': 'Lore',
                       'url': '/api/subclasses/lore'}],
       'url': '/api/spells/magic-missile'}
     _______________________________________________________________________________________
    /\                                                                                      \
(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
    \/______________________________________________________________________________________/


 Candlekeep Monk:
 "Do you need something else?"

 --> [y/n]:
```