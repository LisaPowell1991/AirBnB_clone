#0x01. AirBnB clone - Web static#
##Learning Objectives##
1. What is HTML?
2. How to create an HTML page?
3. What is a markup language?
4. What is the DOM?
5. What is an element / tag ?
6. What is an attribute ?
7. How does the browser load a webpage ?
8. What is CSS ?
9. How to add style to an element ?
10. What is a class ?
11. What is a selector ?
12. How to compute CSS Specificity value ?
13. What are Box properties in CSS ?

##Tasks##
0. Inline styling
Write an HTML page that displays a header and a footer.
Layout:
	Body:
		No margin
		No padding
Header:
		color #FF0000(red)
		Height: 70px
		Width: 100%
	Footer:
		color #00FF00(green)
		Height: 60 px
		Width: 100%
		Text “Best School” center vertically and horizontally
		Always at the bottom at the page
Requirements
You must use the header and footer tags
You are not allowed to import any files
You are not allowed to use the style tag in the head tag
Use inline styling for all your tags

1. Head styling
Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as previous tag)
Requirements:
You must use the header and footer tags
You are not allowed to import any files
No inline styling
You must use the style tag in the head tag
The layout must be the exactly the same as 0-index.html

2. CSS files
Write an HTML page that displays a header and a footer by using CSS files (same as previous task)
Requirements:
You must use the header and footer tags
No inline styling
You must have 3 CSS files:
styles/2-common.css: for global style i.e. the body style
styles/2-header.css: for header style
styles/2-footer.css: for footer style
The layout must be exactly the same as the previous task.

3. Zoning done!
Write an HTML page that displays a header and footer by using CSS files (same as previous code)
Layout:
	Common:
No margin
No padding
Font color: #484848
Font size: 14px
Font family: Circular, “Helvetica Neue”, Helvetica, Arial, sans-serif;
Icon in the browser tab
Header:
color: white
height: 70px
width: 100%
border bottom 1px #CCCCCC
logo align on left and center vertically (20px space at the left)
Footer:
color: white
height: 60px
width: 100%
border top 1px #CCCCCC
text “Best School” center vertically and horizontally
Always at the bottom at the page
Requirements:
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 3 CSS files:
styles/3-common.css: for the global style i.e. body style
styles/3-common.css: for the header style
styles/3-common.css: for the footer style

4. Search!
Write an HTML page that displays a header, footer and a filters box with a search button.
Layout: (based previous task)
	Container:
		between header and footer tags, add a div:
		1. Classname: container
		2. Max width 1000px
		3. Margin top and bottom 30px - it should be 30px under the bottom of the header
		4.Center horizontally
	Filter section:
1. tag section
2. classname filters
3. Inside the .container
4. Color white
5. height: 70px
6. width: 100% of the container
7. Border: 1px #DDDDDD with radius 4px
	Button search:
		1. tag button
		2. text Search
		3. Font size: 18px
		4. Inside the section filters
		5. Background color #FF5A5F
		6. Text color #FFFFFF
		7. Height: 48px
		8. Width: 20% of the section filters
		9. No borders
		10. Border radius: 4px
		11. Center vertically and at 30px of the right border
		12. Change opacity to 90% when the mouse is on the button

Requirements
You must use: header, footer, section, button tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 4 CSS files:
styles/4-common.css: for the global style (body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/4-filters.css: for the filters style

5. More filters
Write an HTML page that displays a header, footer and a filters box.
Layout:
Locations and Amenities filters:
Tag: div
Classname: locations for location tag and amenities for the other
Inside the section filters (same level as the button Search)
Height: 100% of the section filters
Width: 25% of the section filters
Border right #DDDDDD 1px only for the first left filter
Contains a title:
Tag: h3
Font weight: 600
Text States or Amenities
Contains a subtitle:
Tag: h4
Font weight: 400
Font size: 14px
Text with fake contents

Requirements:
You must use: header, footer, section, button, h3, h4 tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 4 CSS files:
styles/4-common.css: for the global style(body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/5-filters.css: for the filters style

6. It's (h)over
Write an HTML page that displays a header, footer and a filters box with dropdown.
Layout:
	Update locations and amenities filters to display a contextual dropdown when the mouse is on the filter div:
tag ul
classname popover
Text should be fake now
Inside each div
Not displayed by default
Color #FAFAFA
Width same as the div filter
Border #DDDDDD 1px with border radius 4px
No list display
Location filter has 2 levels of ul/li;
state->cities
State name must be display in a h2 tag (font size 16px)
Requirements:
You must use: header, footer, section, button, h3, h4, ul, li tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 4 CSS files:
styles/4-common.css: for the global style (body and .container styles)
styles/3-header.css: for the header style
styles/3-footer.css: for the footer style
styles/6-filters.css: for the filters style

7. Display results
Write an HTML page that displays a header, footer, a filters box with dropdown and results.
Layout:
	Add places section:
		tag: section
		classname: places
		Same level as the filters section, inside .container
		Contains a title:
			tag: h1
			text: Places
			Align in the top left
			Font size: 30px
	Contains multiple “Places” as listing (horizontal or vertical) describe by:
		tag: article
		width: 390px
		padding and margin: 20px
		Border #FF5A5F 1px with radius 4px
		Contains the place name:
			Tag: h2
			Font size: 30px
			Center horizontally
Requirements:
	You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
	No inline style
	You  are not allowed to use the img tag
	You are not allowed to use the style tag in the head tag
	All images must be stored in the images folder
	You must have 5 CSS files:
		styles/4-common.css: for the global style
		styles/3-header.css: for the header style
		styles/3-footer.css: for the footer style
		styles/6-filters.css: for the filters style
		styles/7-places.css: for the place's style

8. More details
Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.
Layout:
Add more information to a Place article:
	Price by night:
		Tag: div
		Classname: price_by_night
		Same level as the place name
		Font color: FF5A5F
		Border: #FF5A5F 4px rounded
		min width: 60px
		Height: 60px
		Font size: 30px
		Align: the top right (with space)
Information section:
	Tag: div
	Classname: information
	Height: 80px
	Border: top and bottom #DDDDDD 1px
	Contains (align vertically):
		Number of guests:
			tag: div
			classname: max_guest
			width: 100px
			Fake text
			Icon
	          Number of bedrooms:
			tag: div
			classname: number_rooms
			width: 100px
			fake text
			Icon
	          Number of bathrooms:
			Tag: div
			Classname: number_bathrooms
			Width: 100px
			Fake text
			Icon
User section:
	Tag: div
	Classname: user
	Text Owner: <fake text>
	Owner text should be in bold
Description:
	Tag: div
	Classname: description

Requirements:
You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
No inline style
You are not allowed to use the img tag
You are not allowed to use the style tag in the head tag
All images must be stored in the images folder
You must have 5 CSS files:
	styles/4-common.css: for the global style (i.e. body and .container styles)
	styes/3-header.css: for the header style
	styles/3-footer.css: for the footer style
	stytes/6-fliters.css: for the filters style
 	styles/8-places.css: for the places style


