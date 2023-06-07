from mycode.utils import translate, plot_image

def english_to_pirate():
    input_element = Element("english")
    output_element = Element("output")

    english = input_element.element.value
    pirate = translate(english)
    
    output_element.element.innerText = pirate

def plotter():
    
    input_element = Element("showplot")
    output_element = Element("output")
    
    radius = int(input_element.element.value)
    figure = plot_image(radius)
    display(figure, target="output")

#print("Hello there. How are you today?")
