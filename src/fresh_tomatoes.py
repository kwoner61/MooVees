import webbrowser
import os
import re


def file_to_string(file_path): # Read in entire file content as string
    with open(file_path, 'r') as myfile:
        data = myfile.read()
    return data


current_dir = os.path.dirname(__file__) # Get directory where script is located

# The main page (style and script)
main_page_file = os.path.join(current_dir + '/partials/main.html')
main_page_content = file_to_string(main_page_file)

# A single movie entry html template
movie_tile_file = os.path.join(current_dir + '/partials/movie_content.html')
movie_tile_content = file_to_string(movie_tile_file)


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
