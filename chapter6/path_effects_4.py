import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

fig = plt.figure(figsize=(8, 1))
text_val = fig.text(0.02, 0.5, 'Hatch shadow', fontsize=75, weight=1000, va='center')
text_val.set_path_effects([path_effects.PathPatchEffect(offset=(4, -4), hatch='xxxx',
                                                        facecolor='gray'),
                           path_effects.PathPatchEffect(edgecolor='white', linewidth=1.1,
                                                        facecolor='black')])
plt.show()
