from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from numpy import random

output_file("interactive_plot.html")

source = ColumnDataSource(
        data=dict(
            x=random.randint(100, size=(9)),
            y=random.randint(100, size=(9)),
            desc=['ADINAZOLAM', 'ALPRAZOLAM', 'BROMAZEPAM', 'CHLORDIAZEPOXIDE', 'CLOBAZAM', 
                'CLONAZEPAM', 'CLORAZEPATE_MONOPOTASSIUM', 'DELORAZEPAM', 'DEMOXEPAM'],
            imgs = [
                'resources/images/ADINAZOLAM.png',
                'resources/images/ALPRAZOLAM.png',
                'resources/images/BROMAZEPAM.png',
                'resources/images/CHLORDIAZEPOXIDE.png',
                'resources/images/CLOBAZAM.png',
                'resources/images/CLONAZEPAM.png',
                'resources/images/CLORAZEPATE_MONOPOTASSIUM.png',
                'resources/images/DELORAZEPAM.png',
                'resources/images/DEMOXEPAM.png',
            ]
        )
    )

hover = HoverTool(
        tooltips="""
        <div>
            <div>
                <img
                    src="@imgs" height="200" alt="@imgs" width="200"
                    style="float: left; margin: 15px 15px 15px 15px;"
                    border="0"
                ></img>
            </div>
            <div>
                <span style="font-size: 14px; font-weight: bold;">@desc</span>
            </div>
        </div>
        """
    )

p = figure(plot_width=600, plot_height=600, tools=[hover],
           title="Interactive plot")

p.circle('x', 'y', size=20, source=source)

show(p)