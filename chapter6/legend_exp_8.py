import matplotlib.pyplot as plt
import matplotlib.patches as m_patches


class AnyObject(object):
    pass


class AnyObjectHandler(object):
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        patch = m_patches.Rectangle([x0, y0], width, height, facecolor='red',
                                    edgecolor='black', hatch='xx', lw=3,
                                    transform=handlebox.get_transform())
        handlebox.add_artist(patch)
        return patch


plt.legend([AnyObject()], ['My first handler'],
           handler_map={AnyObject: AnyObjectHandler()})
plt.show()
