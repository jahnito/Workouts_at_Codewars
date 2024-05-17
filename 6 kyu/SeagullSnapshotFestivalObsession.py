'''
Seagull Snapshot Festival

The town of Landgull is celebrating its annual Seagull Snapshot Festival, and you've recently developed an obsession with seagulls, so it's the perfect oportunity to take some nice pictures of your favourite animal.

Your camera looks like this:

[[   x   ]]

The view of the sea without a seagull looks like this:

..·.···...·.·.·...···.·..·

The view of the sea with a seagull over it looks like this:

..·.···..seagull..···.·..·

Once you've taken a picture of the seagull, it should look like this.

..·.···[[seaxull]]···.·..·
Your goal

We'll provide a nice view with (at most) one seagull in it. Your goal is to take a snapshot of the seagull, if there's any.

Your camera can't step outside of the field of view, but seagulls may be partially outside of it. If they are, just catch as much of the seagull as possible (i.e. place your camera right at the edge, even if the seagull is not centred within it).

If the scene is too thin or there's no seagull in it, just wait until next time (i.e. return the same view without placing a camera on top of it).
'''


def snapshot(scene: str) -> str:
    traf = '[[***x***]]'
    def replacer(scene: str, where: str):
        if where == "Start":
            return ''.join([i if i != '*' else j for i, j in zip(traf + '*' * (len(scene) - len(traf)), scene)])
        elif where == "End":
            return ''.join([i if i != '*' else j for i, j in zip('*' * (len(scene) - len(traf)) + traf, scene)])
        elif where == "Middle":
            s = scene.find('s') - 2
            e = len(scene) - (s + len(traf))
            return ''.join([i if i != '*' else j for i, j in zip('*' * s + traf + '*' * e, scene)])
    if len(traf) > len(scene):
        return scene
    elif any([True if i in 'seagull' else False  for i in scene[:3]]):
        return replacer(scene, "Start")
    elif any([True if i in 'seagull' else False  for i in scene[-3:]]):
        return replacer(scene, "End")
    elif all([True if i not in 'seagull' else False for i in scene]):
        return scene
    else:
        return replacer(scene,"Middle")


if __name__ == '__main__':
    print(snapshot(".·..·····seagull·..·"))
    print(snapshot("···..·...··...··..seagu"))
    print(snapshot("ull·..··..·..·..·..·"))
    print(snapshot("·seagull·."))
