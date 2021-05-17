from django.db import models

class Post(models.Model):

	class Meta:
		verbose_name = "Пост"
		verbose_name_plural = "Посты"

	title = models.CharField(max_length = 255)

	description = models.TextField()

	url = models.URLField()


	def __str__(self):
		return f'Пост с названием \"{self.title}\"'


	def link_for_video(self):
		url = str(self.url)

		video_id = url.split('/')[-1]

		link = 'https://www.youtube.com/embed/' + video_id

		return link


class Product(models.Model):

	class Meta:
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"

	title = models.CharField(max_length = 255)

	description = models.TextField()

	image = models.ImageField(upload_to = 'imgs/')

	def __str__(self):
		return f'Продукт с названием "{self.title}"'


class DocumentationBlock(models.Model):

	class Meta:
		verbose_name = "Блок документации"
		verbose_name_plural = "Блоки документации"

	title = models.CharField(max_length = 255)

	def __str__(self):
		return f'Блок документации "{self.title}"'


class DocumentationBlockItem(models.Model):

	class Meta:
		verbose_name = "Элемент блока документации"
		verbose_name_plural = "Элементы блока документации"

	documentation_block = models.ForeignKey(DocumentationBlock, on_delete = models.CASCADE)

	file = models.FileField(upload_to = 'documents/')

	def __str__(self):
		return f'Элемент {self.file.name} блока {self.documentation_block}'


class TrialsPhoto(models.Model):

	class Meta:
		verbose_name = "Фото испытаний"
		verbose_name_plural = "Фото испытаний"

	image = models.ImageField(upload_to = 'trialsphotos/')

	def __str__(self):
		return f'Фото испытаний {self.image.name}'