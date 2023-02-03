#* FİLTER için; (dj-08)
# yazılan kelimenin aynısını arar,
# mesela name için data içinde cooper varsa coop yazınca bulmaz.

pip install django-filter
pip freeze > requirements.txt


#todo, A- Eğer Djangonun default FILTER ayarlarını kullanacaksak, iki farklı şekilde yapılabilir,
        #! 1 - settings içine ekleyerek;
                  INSTALLED_APPS = [ 'django_filters', ] # içine ekle
                  # en sonuna uygun bir yere DEFAULT_FILTER_BACKENDS ekle,
                  # eğer önceden REST_FRAMEWORK = { } varsa onun içine ekle, yoksa üstteki çalışmaz.
                  #? böyle yapınca global alanda tanımlanmış olur ve onu kullanır,

                  REST_FRAMEWORK = {
                      'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
                  }
                  
                  # view'da filterset_fields ekleyip, filitrelenecek alanları yazıyoruz,
                  filterset_fields = ["id", "first_name", "last_name"]

        #! 2 - views içinde import ederek
                  # settings içine birşey yazmaya gerek yok,
                  # fakat yazılsa bile local alanda olan globalı ezeceğinden import edilen çalışacaktır.
                  
                  from django_filters.rest_framework import DjangoFilterBackend

                  # view'da filter_backends ve filterset_fields ekleyip, filitrelenecek alanları yazıyoruz,
                  filter_backends = [DjangoFilterBackend]                 #? hangi filitrelemeyi kullanacak,
                  filterset_fields = ["id", "first_name", "last_name"]    #? nerede filitrelemeyi kullanacak,
                  # (hangisini kullanacaksan adını yaz)

#todo, B- Djangonun default ayarları dışında customize bir FILTER kullanmak için, filter.py ekle;
#? böyle yapınca localde çalışır ve global olanı ezer, yani settings içinde yazılsa bile burada yazılan çalışır,
# daha sonra paginationda yapıldığı gibi default filter ayarları miras alınarak custom bir filter yazılabilir,
# view'da import edilip kullanılabilir