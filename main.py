from flet import *

def main(page:Page):
	page.window_width = 400

	mycontent= Column(scroll="auto")
	def youlongstart(e:LongPressStartEvent):
		# AND IF YOU CLICK LONG Container mycontent
		# THEN CHANGE BGCOLOR 
		e.control.content.bgcolor="blue200"
		# CHANGE TEXT TITLE AppBar
		page.controls[0].title.value = "select Option"
		page.controls[0].bgcolor = "blue200"

		# AND SHOW HIDE IconButton IN APPBAR
		page.controls[0].actions[1].visible = True
		page.controls[0].actions[3].visible = True

		page.update()


	# ADD DATA TO mycontent
	mycontent.controls.append(
		Row([
			GestureDetector(
				# FOR LONG PRESS USE THIS METHOD
			on_long_press_start=youlongstart,
			content=Container(
			margin=margin.only(top=30),
			bgcolor="green",
			padding=10,
			alignment=alignment.center,
			content=Text("this text for copy",
				size=25,color="white"
				)
				)
				)

			],alignment="center")

		)



	def selectall(e):
		# NOW IF YOU SELECT All THEN
		# CHANGE ALL CONTENT IN mycontent TO BGCOLOR BLUE
		for i,x in enumerate(mycontent.controls):
			x.controls[0].content.bgcolor ="blue200"

		page.controls[0].actions[2].visible = True
		page.controls[0].actions[3].visible = True
		page.update()

	def deleteall(e):
		# AND LAST CREATE DELETE FOR DELETE SELECTED 
		# or all SELECT
		mycontent.controls.clear()
		page.controls[0].actions[2].visible = False
		page.controls[0].actions[3].visible = False

		page.snack_bar = SnackBar(
			content=Text("Success delete all",size=30),
			bgcolor="red"
			)
		page.snack_bar.open = True
		page.update()



	def addduplicate(e):
		# AND NOW CREATE FUNCTION DUPLICATE
		mycontent.controls.append(
		Row([
			GestureDetector(
				# FOR LONG PRESS USE THIS METHOD
			on_long_press_start=youlongstart,
			content=Container(
			margin=margin.only(top=30),
			bgcolor="green",
			padding=10,
			alignment=alignment.center,
			content=Text("this text for copy",
				size=25,color="white"
				)
				)
				)

			],alignment="center")

		)
		# AND AFTER COPY THEN CHANGE BGCOLOR TO GREEN AGAIN
		for i,x in enumerate(mycontent.controls):
			x.controls[0].content.bgcolor = "green"

		page.controls[0].title.value = "books app"
		page.controls[0].bgcolor = "yellow"
		page.controls[0].actions[1].visible = False
		page.controls[0].actions[3].visible = False

		page.update()



	def cancelall(e):
		# NOW CREATE FUNCTION CANCEL ALL
		# IF YOU CLICK CROSS ICON THEN ALL WILL CANCELL
		# THEN CHANGE BGCOLOR TO GREEN AGAIN
		for i,x in enumerate(mycontent.controls):
			x.controls[0].content.bgcolor = "green"
		page.controls[0].actions[1].visible = False
		page.controls[0].actions[2].visible = False
		page.controls[0].actions[3].visible = False
		page.controls[0].title.value = "Books app"
		page.controls[0].bgcolor ="yellow"
		page.update()




	page.add(
		AppBar(
		title=Text("Books app",color="black",
			weight="bold"
			),
		bgcolor="yellow",
		actions=[
		IconButton(icon="select_all",
			icon_size=30,icon_color="black",
			on_click=selectall
			),
		IconButton(icon="content_copy",
			icon_size=30,icon_color="black",
			on_click=addduplicate,
			visible=False
			),
		IconButton(icon="delete",
			icon_size=30,icon_color="black",
			on_click=deleteall,
			visible=False
			),
		IconButton(icon="close",
			icon_size=30,icon_color="black",
			on_click=cancelall,
			visible=False
			),


		]

			),
		mycontent
		)

flet.app(target=main)
