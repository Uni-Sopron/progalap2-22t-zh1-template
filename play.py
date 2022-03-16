
class Play:
    pass


class Scene:
    pass


# Példakód az osztályok és metódusaik használatára
if __name__ == '__main__':
    play = Play('William Shakespeare', 'Hamlet', './hamlet')
    print('Horatio appears in', play.scene_count('Horatio'), 'scenes')  # 2
    print('Hamlet appears in', play.scene_count('Hamlet'), 'scenes')  # 1
    print('Arthur appears in', play.scene_count('Arthur'), 'scenes')  # 0

    scene1 = Scene('hamlet/act-1-scene-1.txt')
    hamlet1 = scene1.speech_count('Hamlet')
    print('Hamlet speaks', hamlet1, 'times in Scene 1')  # 0

    scene2 = Scene('hamlet/act-1-scene-2.txt')
    hamlet2 = scene2.speech_count('Hamlet')
    print('Hamlet speaks', hamlet2, 'times in Scene 2')  # 33

    cameo = scene2.speech_count('Shakespeare')
    print('Shakespeare speaks', cameo, 'times in Scene 2')  # 0

    missing = Scene('hamlet/act-666-scene-45.txt')  # error message

    play.show_charts()
