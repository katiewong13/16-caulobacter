def plot_area(area):
    '''Plot area of the bacteria as found from functions in area.py'''
    r = list(range(0, len(area)))
    
    # Create the labeled figure for first bacterium, stored in variable `p_1`
    p = bokeh.plotting.figure(
        width=400,
        height=300,
        x_axis_label='Frame Number',
        y_axis_label= 'Area Taken up by bacterium'
    )

    p.circle(
        legend = "Labeled",
        x = r,
        y = area,
        color = 'orange'
    )
    bokeh.io.show(p)
    return

  
def plot_growth_identifier(df):
    '''Plot '''
    hv.Points(data = df,
         kdims = ['time (min)', 'area (µm²)'],
         vdims = ['growth identifier'],
        ).groupby('growth identifier'
        ).opts(tools = ['hover'], height=400, width=700, 
               legend_position ='top_right', 
               title = 'Bacterium Area vs. Time w/ Growth Identifier'
        ).overlay()
    return

    
def plot_growth_ecdf(df_dt):
    p = bokeh_catplot.ecdf(data = df_dt,
                      cats = None,
                      val = 'Time between divisions (in min)',
                      style = 'staircase',
                      title = 'Time Between Divisions for Bacterium 1')
    bokeh.io.show(p)
    return