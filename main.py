from flask import Flask, render_template, request

# model
class modelMahasiswa: 
	def __init__(self, nama, umur, jurusan):
		self.nama = nama
		self.umur = umur
		self.jurusan = jurusan


# view
class viewMahasiswa:
	def showData(self, mahasiswa):
		return render_template("mahasiswa.html",mahasiswa=mahasiswa)


# controler
class controlerMahasiswa:
	def __init__(self, model, view):
		self.model = model
		self.view = view

	def set_nama(self, nama):
		self.model.nama = nama
	
	def set_umur(self, umur):
		self.model.umur = umur

	def set_jurusan(self, jurusan):
		self.model.jurusan = jurusan

	def update_view(self):
		return self.view.showData(self.model)


# ini adalah aplikasi flask nya
app = Flask("Rifa")

@app.route("/mahasiswa", methods = ["GET", "POST"])
def mahasiswa():
	mahasiswa = modelMahasiswa("Rifa'i Sopyan", "21", "Kimia")
	view = viewMahasiswa()
	controler = controlerMahasiswa(mahasiswa, view)

	if request.method == "POST":
		controler.set_nama(request.form["nama"])
		controler.set_umur(request.form["umur"])
		controler.set_jurusan(request.form["jurusan"])

	return controler.update_view()

if __name__ == "__main__":
	app.run()