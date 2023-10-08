% Normal pokemons
pokemon(pidgey).
pokemon(pidgeotto).
pokemon(pidgeot).
pokemon(mega_pidgeot).

pokemon(rattata).
pokemon(alola_rattata).
pokemon(raticate).
pokemon(alola_raticate).

% Water pokemons
pokemon(squirtle).
pokemon(wartortle).
pokemon(blastoise).

pokemon(psyduck).
pokemon(golduck).

% Grass pokemons
pokemon(bulbasaur).
pokemon(ivysaur).
pokemon(venusaur).

pokemon(oddish).
pokemon(gloom).
pokemon(vileplume).
pokemon(bellossom).

% Fire pokemons
pokemon(growlithe).
pokemon(arcanine).

pokemon(ponyta).
pokemon(rapidash).

% Family connections
parent(pidgey, pidgeotto).
parent(pidgeotto,pidgeot).
parent(pidgeot, mega_pidgeot).

parent(rattata, alola_rattata).
parent(alola_rattata, raticate).
parent(raticate, alola_raticate).

parent(squirtle, wartortle).
parent(wartortle, blastoise).

parent(psyduck, golduck).

parent(bulbasaur, ivysaur).
parent(ivysaur, venusaur).

parent(oddish, gloom).
parent(gloom, vileplume).
parent(gloom, bellossom).

parent(growlithe, arcanine).

parent(ponyta, rapidash).

% Pokemon types
type(normal).
type(water).
type(grass).
type(fire).

pokemon_type(pidgey, normal).
pokemon_type(rattata, normal).
pokemon_type(squirtle, water).
pokemon_type(psyduck, water).
pokemon_type(bulbasaur, grass).
pokemon_type(oddish, grass).
pokemon_type(growlithe, fire).
pokemon_type(ponyta, fire).

% Rules
grand_parent(X,Y) :- parent(X,Z), parent(Z, Y).
grand_son(X,Y) :- parent(Y,Z), parent(Z, X).
predecessor(X,Y) :- parent(X, Y).
predecessor(X, Y) :- parent(X, Z), predecessor(Z, Y).
descendant(X, Y) :- parent(Y, X).
descendant(X,Y) :- parent(Y, Z), predecessor(Z, X).
relative(X, Y) :- predecessor(X, Y); descendant(X, Y).

which_type(X, Y) :- pokemon_type(Y, X).
which_type(X, Y) :- predecessor(Z, Y), pokemon_type(Z, X). 




