from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return '''
    <html>

    	<h1>Welcome to Nadav's gallery!</h1>
    	<p>this is a photo gallery containing three types of photos: food, pets, and outer space.</p>
    	<a href = "/food1">go to the first food photo</a>
    	<br>
    	<a href = "/pet1">go to the first pet photo</a>
    	<br>
    	<a href = "/space1">go to the first space photo</a>


    </html>
    '''

@app.route("/food1")
def food1():
	return '''
	<html>

		<img src = "https://vancouverwithlove.com/wp-content/uploads/2023/08/pasta-al-pesto-24-1.jpg" width = "300px">
		<br>
		<a href = "/food2">Next food</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''

@app.route("/food2")
def food2():
	return '''
	<html>

		<img src = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/steamed-pork-buns-8f10f37.jpg?quality=90&resize=440,400" width = "300px">
		<br>
		<a href = "/food1">Previous food</a>
		<br>
		<a href = "/food3">Next food</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''

@app.route("/food3")
def food3():
	return '''
	<html>

		<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBFCimCM1wFvb3FZQOZH_j5ta4Qd2SlNj2vg&s" width = "300px">
		<br>
		<a href = "/food2">Previous food</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''


@app.route("/pet1")
def pet1():
	return '''
	<html>

		<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtRqsbpNzTz8wXYvdqnFq9VRcj5uBoeaM13w&s" width = "300px">
		<br>
		<a href = "/pet2">Next pet</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''

@app.route("/pet2")
def pet2():
	return '''
	<html>

		<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzySO8TACxxZVykdof7q6tJYrA8c_XfgGV8w&s" width = "300px">
		<br>
		<a href = "/pet1">Previous pet</a>
		<br>
		<a href = "/pet3">Next pet</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''

@app.route("/pet3")
def pet3():
	return '''
	<html>

		<img src = "https://cdn.animalsaustralia.org/wp-content/uploads/2021/11/25114441/55d6d12b3e5b61440141611-900x900.jpg?theia_smart_thumbnails_file_version=2" width = "300px">
		<br>
		<a href = "/pet2">Previous pet</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''


@app.route("/space1")
def space1():
	return '''
	<html>

		<img src = "https://c.files.bbci.co.uk/16BB/production/_110891850_pia23645_index.jpg" width = "300px">
		<br>
		<a href = "/space2">Next space</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''

@app.route("/space2")
def space2():
	return '''
	<html>

		<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjh5B2IFnWjADWsE2qNcRowv6IYNomyNQaKg&s" width = "300px">
		<br>
		<a href = "/space1">Previous space</a>
		<br>
		<a href = "/space3">Next space</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''

@app.route("/space3")
def space3():
	return '''
	<html>

		<img src = "https://i.natgeofe.com/k/1ef0d42f-adf7-49e7-a2de-7d381fd18f95/moon-landing-textimage_square.png" width = "300px">
		<br>
		<a href = "/space2">Previous space</a>
		<br>
		<a href = "/home">Back to home</a>

	</html>'''


if __name__ == '__main__':
    app.run(debug=True)