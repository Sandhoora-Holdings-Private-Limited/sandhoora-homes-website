##Runs on python 3.5.x
import os
from PIL import Image


def make_galary():
    galary = 'images/galary/'
    lines_written = 0
    return_string = ""
    for project in next(os.walk(galary))[1]:
        project_link = galary + project + '/'
        icon_link = project_link + 'icon/' + next(os.walk(project_link + 'icon/'))[2][0]
        files = next(os.walk(project_link))[2]
        links = []
        for link in files:
            links.append(project_link + link)

        string,line_count = make_galary_item(icon_link,links)
        return_string += string
        lines_written += line_count

    return return_string,lines_written

def make_galary_item(icon_link,links,title="",caption=""):
    return_string = '           <div class = "gallery-item">\n'
    return_string += '              <a class="example-image-link" onclick="galary_function(' + make_galary_parameter(links) + ')" data-lightbox="example-set" data-title="' + title + '">\n'
    return_string += '                  <div class="grid">\n'
    return_string += '                      <figure class="effect-apollo">\n'
    return_string += '                          <img src="' + icon_link + '" alt="' + title + '"/>\n'
    return_string += '                              <figcaption>' + caption + '</figcaption>\n'
    return_string += '                     </figure>\n'
    return_string += '                 </div>\n'
    return_string += '                <a>\n'
    return_string += '         </div>\n'
    lines_written = 10
    return return_string,lines_written

def make_galary_parameter(links):
    return_string = '['
    for link in links:
        if not link[-5:] == "Store":
            w,h = get_dimentions(link)
            return_string += '{src: \'' + link + '\',w: ' + str(w) + ',h: ' + str(h) + '},'
    return_string = return_string[:-1]
    return_string += ']'
    
    return return_string

def get_dimentions(link):
    pic = Image.open(link)
    w,h = pic.size
    pic.close()
    return w,h

infile = 'index_in.html'
outfile = 'index.html'
print('Reading from : '+ infile)
index_in_file = open(infile, 'r')
print('Writing to : ' + outfile)
index_out_file = open(outfile, 'w')
line = index_in_file.readline()
lines_read = 1
lines_written = 0
write = True

while not line == "</html>":
    if write:
        index_out_file.write(line)
        lines_written += 1

    if line == "<!--Galary_code_starts_here_marker-->\n":#first code starting pint
        gallary_code_start_line = lines_written
        write_string,line_count = make_galary()
        index_out_file.write(write_string)
        lines_written += line_count 
        write = False
    elif line == "<!--Galary_code_ends_here_marker-->\n":#first code ending point
        index_out_file.write(line)
        lines_written += 1
        Galary_code_ends_line = lines_written
        write = True  
        
    line = index_in_file.readline()
    lines_read += 1

    print_string = 'read : ' + str(lines_read) + ' | wriiten : ' + str(lines_written)
    print(print_string)

index_out_file.write('</html>')
lines_written += 1
print( 'read : ' + str(lines_read) + ' | wriiten : ' + str(lines_written) )
print('modeified code between : ' + str(gallary_code_start_line) + ' | ' + str(Galary_code_ends_line))
index_in_file.close()
index_out_file.close()
print("Done!")