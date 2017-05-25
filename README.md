
`main.py` is the main program.

`analysis.py` evaluates the randomiser-generated sequences according to a number of metrics.

`compare.py` performs a multidimensional distance comparison, in an attempt to quantify the similarity of the randomisers based on the reported metrics.

`testgame.py` is a TAP-like game for testing the randomisers. It uses [pygame](http://pygame.org).

The `piecedata` directory contains rotation system data.

`randos` directory contains the randomisers.

The following randomisers were implemented when this was forked:
* `bag.py` implements the 7-piece bag mandated by the Tetris Guideline.
* `bag2.py` implements a 14-piece bag (2 7-piece bags shuffled together).
* `deepbag.py` implements a pair of 7-piece bags where the first bag is used for drawing pieces and is replenished by the second bag on every draw.
* `flatbag.py` implements a fixed bag order. The piece sequence here is deterministic and cycles with period 7.
* `foreverbag.py` implements a 4-piece bag which is replenished by a fixed sequence of pieces.
* `fullrandom.py` implements a memoryless randomiser.
* `nes.py` implements an idealised version of the Nintendo NES Tetris randomiser.
* `tap.py` implements the randomiser seen in Tetris The Absolute The Grand Master 2 PLUS (verify if this was in the original TA).
* `tgm.py` implements the randomiser seen in Tetris The Grand Master.
* `ti.py` implements the randomiser seen in Tetris The Grand Master 3 Terror-Instinct.

The following randomisers have been implemented after the fork:
* The following are instances of `bag`:
    * `bag28.py` implements a 28-piece bag (4 7-piece bags shuffled together).
    * `bag63.py` implements a 63-piece bag (9 7-piece bags shuffled together).
* `fractionbag.py` implements a bag which consists of some number of fixed bags plus part of a bag shuffled together. The following are instances of this randomiser:
    * `bag8.py` implements an 8-piece bag, constructed as a 7-piece bag with a bonus piece randomly added before shuffling.
    * `bag10.py` implements a 10-piece bag, constructed as a 7-piece bag with three pieces from another 7-piece bag added before shuffling.
* `partialbag.py` implements a "partial bag" randomiser, where the bag is replaced when a certain number of pieces (less than the bag size) have been drawn. The following are instances of this randomiser:
    * `bag5.py` implements a 5-piece bag drawn from a 7-piece bag.
    * `bag6.py` implements a 6-piece bag drawn from a 7-piece bag. This is also the default of `partialbag.py`.
* `dtet.py` implements the DTET randomiser. In the future this will be reimplemented as an instance of a future "weight" randomiser (pending a name).

The following randomisers are pending implementation:
* `ccs.py` implements the randomiser from Tetris with Cardcaptor Sakura: Eternal Heart.
* `historygeneric.py` implements a generic history randomiser. Note that the TGM series randomisers use their own PRNGs instead of Python's (Mersenne Twister) and hence are not instances of this. The following are instances of this randomiser:
    * `history3strict.py` implements a history of length 3 and strict exclusion (infinite rolls).
    * `history4roll2.py` implements a history of length 4 and rolls at most 2 times.
    * `history4roll4.py` implements a history of length 4 and rolls at most 4 times. This is equivalent to TGM's randomiser apart from the PRNG algorithm.
    * `history4roll6.py` implements a history of length 4 and rolls at most 6 times. This is equivalent to TGM2's randomiser apart from the PRNG algorithm.
    * `history4strict.py` implements a history of length 3 and strict exclusion (infinite rolls).
* `notgb.py` is a weighted history randomiser where the last piece has weight 2 and the rest have weight 5. This was once claimed to be the algorithm used in the Game Boy game (it isn't).
* `refillbag.py` implements a "refill" bag randomiser, where the bag is refilled when a certain number of pieces (less than the bag size) have been drawn. Generally this refill comes from another bag. This was first proposed by Okey_Dokey on the Hard Drop forums The following are instances of this randomiser:
    * `bag8refill7.py` implements an 8-piece bag that is refilled from a 7-piece bag when one piece remains.
    * `bag14refill7.py` implements a 14-piece bag that is refilled from a 7-piece bag when one piece remains.
* The following instances of `partialbag` are pending implementation:
    * `bag7from8.py` implements a 7-piece bag drawn from an 8-piece bag (initialised as in `bag8`).
    * `bag10from14.py` implements a 10-piece bag drawn from a 14-piece bag.
* `speedblocks.py` implements SpeedBlocks' randomiser. This randomiser is a weighted randomiser that iteratively adjusts the weights after each piece (http://harddrop.com/forums/index.php?showtopic=7795&hl=randomizer&st=15)