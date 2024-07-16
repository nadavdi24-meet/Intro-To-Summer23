function changeBackgroundColor() {
	var fav_col = document.querySelector('input[name="color"]:checked').id;
	console.log(fav_col);
	if (fav_col == "fav_col_green") {
		fav_col = "green"
	} else if (fav_col == "fav_col_red") {
		fav_col = "red"
	}  else if (fav_col == "fav_col_blue") {
		fav_col = "blue"
	}
	document.getElementsByTagName("body")[0].style.backgroundColor = fav_col;
}