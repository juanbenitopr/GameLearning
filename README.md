# GameLearning

Game Learning is a project focus on trainning your machine learning concepts. it has a few modules which implements a simple game logic, and other module where you use machine learning estimator to try predict the next values.

The game is played the next way:

1. You have some rocks in a bottle, there are some rocks white and one black.
2. For each white rock you get from the bottle you will win among money (how much money is random), if you get the black rock you lose, and you don't get anything.
3. The objective of this game is win all the possible money, and stop before get the black rock.

You have tree modules:
    
1. the_big_game
2. generate_random_games
3. learning_game

Intructions: 
1. I provide a training samples, it is called myfile.json and one scikit_model packaged into pickle file.
2. You have to install the requirements.txt, it will be installed by the next command: pip install -r path/to/requirements.txt
3. Then you can run the_big_game, and check the results displayed from command promt.
4. If you want to create your own samples training, you have to run generate_random_games.py, and learning_game.py, then other myfile.json and clp.pickle will be generated.
5. You should touch all the components, try differents estimators, want to get metrics, try other game, and so on.

If you want to colaborate with this repository you only have to do a pull request!
