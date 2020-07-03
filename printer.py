def print_code(game):
    game.log += ("++++++++++++++++++++++++")
    game.log += '\n'

    text = "CODE : " + str(game.codemaker.code)
    game.log += text + "\n" 

    print_knowledge(game, False)
    game.log += ("++++++++++++++++++++++++")
    game.log += '\n'


def print_game_state(i, move, feedback, game):
    game.log += ("++++++++++++++++++++++++")
    game.log += '\n'

    text = "Move : " + str(i) + " : " + str(move)
    game.log += text + "\n"

    text = "Feedback : " + str(feedback)
    game.log += text + "\n"
    print_knowledge(game)
    game.log += ("++++++++++++++++++++++++")
    game.log += '\n'


def print_winner(winner):
    game.log += ("++++++++++++++++++++++++")
    game.log += '\n'

    text = "WINNER : " + winner
    game.log += text + "\n"

    game.log += ("++++++++++++++++++++++++")
    game.log += '\n'


def print_knowledge(game, print_worlds=True):
    game.log += ('\n')
    game.log += '\n'

    text = "Total worlds possible after this move : " + \
        str(len(game.knowledge_manager.model.worlds))
    game.log += text + "\n"
    game.log += ('\n')
    game.log += '\n'

    if print_worlds:
        for w in game.knowledge_manager.model.worlds:
            game.log += (str(w.name) + str(w.assignment))
            game.log += '\n'

    game.log += ('\n')
    game.log += '\n'
    game.log += ("Real World : " + str(game.knowledge_manager.real_world))
    game.log += '\n'
    game.log += ("Number of Relations for Agent 1 : " + \
          str(len(game.knowledge_manager.model.relations['1'])))
    game.log += '\n'
    game.log += ("Number of Relations for Agent 2 : " + \
          str(len(game.knowledge_manager.model.relations['2'])))
    game.log += '\n'
    game.log += ('\n')
    game.log += '\n'

    text = "Code Maker Knowledge : "
    game.log += text + "\n"
    game.log += str(game.agent_knowledge.agent1)
    game.log += '\n'
    game.log += ('\n')
    game.log += '\n'

    text = "Code Breaker Knowledge : "
    game.log += text + "\n"
    game.log += str(game.agent_knowledge.agent2)
    game.log += '\n'
    game.log += ('\n')
    game.log += '\n'

    text = "Common Knowledge : "
    game.log += text + "\n"
    game.log += str(game.agent_knowledge.common_knowledge)
    game.log += '\n'
    game.log += ('\n')
    game.log += '\n'


def print_simulation_results(strategy_analyser):
    game.log += ("++++++++++++++++++++++++")
    game.log += '\n'
    game.log += ("Total games run for each strategy : " + \
          strategy_analyser.number_of_games)
    game.log += '\n'
    game.log += ('\n')
    game.log += '\n'

    game.log += ("Games won by Mathematician Code Breaker : " + \
          strategy_analyser.mathematician_codebreaker_score)
    game.log += '\n'
    game.log += ("Games won by Logician Code Breaker : " + \
          strategy_analyser.logician_codebreaker_score)
    game.log += '\n'
    game.log += ("Games won by Random Code Breaker : " + \
          strategy_analyser.random_codebreaker_score)
    game.log += '\n'
    game.log += ("++++++++++++++++++++++++")
    game.log += '\n'
