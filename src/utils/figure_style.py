import matplotlib.pyplot as plt
import seaborn as sns

class FigureStyle:
    def __init__(self, 
                 palette='colorblind', 
                 context='notebook', 
                 style='white', 
                 font='Helvetica', 
                 fontsize=6, 
                 dpi=300,
                 linewidth=0.85,
                 markersize=1,
                 tick_major_pad=0,
                 colors=None  # New parameter for custom colors
                ):
        self.palette = palette
        self.context = context
        self.style = style
        self.font = font
        self.fontsize = fontsize
        self.dpi = dpi
        self.max_width_inches = 7.0  # Convert 180 mm to inches
        self.linewidth = linewidth
        self.markersize = markersize
        self.tick_major_pad = tick_major_pad
        self.custom_colors = colors  # Store custom colors

    def apply(self):
        if self.custom_colors:
            sns.set_palette(self.custom_colors.values())
        else:
            sns.set_palette(self.palette)
        rc_params = {
            "font.size": self.fontsize,
            "axes.titlesize": self.fontsize + 1,
            "axes.labelsize": self.fontsize,
            "xtick.labelsize": self.fontsize,
            "ytick.labelsize": self.fontsize,
            "legend.fontsize": self.fontsize,
            "lines.linewidth": self.linewidth,
            "axes.linewidth": self.linewidth,
            "lines.markersize": self.markersize,
            'xtick.major.pad': self.tick_major_pad,
            'ytick.major.pad': self.tick_major_pad,
            'pdf.fonttype': 42, # IMPORTANT: This is to make the pdf editable by Adobe Illustrator
            'ps.fonttype': 42, # IMPORTANT: This is to make the pdf editable by Adobe Illustrator
            "font.family": self.font
        }
        sns.set_context(self.context, rc=rc_params)
        sns.set_style(self.style)
        plt.rcParams.update(rc_params)

    def update_legend_style(self, ax, legend_title=None, clean_handles=False, **kwargs):
        legend = ax.legend(**kwargs)
        if legend_title is None:
            legend.set_title(legend.get_title().get_text(), prop={'size': self.fontsize, 'weight': 'bold'})
        else:
            legend.set_title(legend_title, prop={'size': self.fontsize , 'weight': 'bold'})
        if clean_handles:
            handles, labels = ax.get_legend_handles_labels()
            new_labels = [label.replace('_', ' ') for label in labels]
            ax.legend(handles=handles, labels=new_labels)
        return legend

    def set_titles(self, ax, title, fontsize=None):
        if fontsize is None:
            fontsize = self.fontsize + 1
        ax.set_title(title, fontsize=fontsize, weight='bold')

    def set_labels(self, ax, xlabel, ylabel):
        ax.set_xlabel(xlabel, fontsize=self.fontsize + 1, weight='bold')
        ax.set_ylabel(ylabel, fontsize=self.fontsize + 1, weight='bold')

    def save_figure(self, filename, tight_layout=True, trim_margin=True, **kwargs):
        fig = plt.gcf()
        current_size = fig.get_size_inches()
        if current_size[0] > self.max_width_inches:
            scale_ratio = self.max_width_inches / current_size[0]
            fig.set_size_inches(self.max_width_inches, current_size[1] * scale_ratio)
        if tight_layout:
            plt.tight_layout()

        if trim_margin:
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight', pad_inches=0.1, **kwargs)
        else:
            plt.savefig(filename, dpi=self.dpi, **kwargs)

    def get_palette_colors(self, n_colors):
        return sns.color_palette(self.palette, n_colors)
