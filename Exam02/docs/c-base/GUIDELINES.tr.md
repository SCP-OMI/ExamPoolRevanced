# Genel Kurallar

* Hangi sebeple olursa olsun herhangi birisiyle iletişim kurmak yasaktır.

* Şu anda sınavdasınız, mesajlaşamazsınız, müzik dinleyemezsiniz, ses çıkartamazsınız veya diğer öğrencilere rahatsızlık verebilecek hiçbir şey yapamazsınız.

* Telefonlarınız ve tüm teknolojik aletleriniz kapalı ve uzakta olmalıdır. Eğer telefonunuz herhangi bir şekilde çalarsa, bulunduğunuz sıradaki herkes diskalifiye edilir ve sınavdan atılır.

* Ana dizininiz 3 dizinden oluşuyor: "rendu", "subjects" and "traces".

* "Subjects" kısmında görevlerinizin açıklamaları bulunmaktadır.

* Rendu dosyası Git 'e yüklediğiniz repository'nin klonudur. Bunun içinde çalışıp normal bi repository olarak kullanabilirsiniz.

* Sistem git üzerinedeki doğru yere pushlanmayan hiçbir şeyi notlandırmayacaktır. Examshell'in size dosyanızı nereye koyacağınızı söylediği yere dikkat edin.

* Programlarınızı sadece 'rendu' dizininde(ya da alt dizinlerinde) çalıştırabilirsiniz.

* Bazı çalışmaları tamamlayabilmek için man'ı okumanız gerekebilir...

* Bir program tarafından notlandırılacaksınız. Belirtilen dosya/yol/fonksiyon isimlerine dikkat etmeniz gerekmektedir.

* Çalışmalarınızda hangi dosyaların toplanacağı belirtilecek.

* Eğer bir çalışma spesifik bir dosyada çalışmanızı gerektiriyorsa, bu dosya kendini belli etmesi için özellikle isimlendirilecek. Örnek vermek gerekirse: "file1.c file1.h".

 * Aksi takdirde dosya isimleri size bırakıldığı zaman, çalışmada size dosyanızın hangi uzantıda olacağını belirtilecek.

 * Makefile'a gerek olduğunda HER ZAMAN açıkça belirtilecektir.

* Teknik bir sorunla karşılaştığınızda ya da herhangi bir sorunuz olduğunda, sessizce ayağa kalkıp görevlilerden birinin yanınıza gelmesine bekleyin. Yanınızdaki arkadaşlarınıza soru sormak veya sesli bir şekilde görevlilere seslenmek kesinlikle yasaktır.

* İzin verilmeyen her türlü eşya yasaktır.

* Çıktıktan sonra sınava bir daha giremezsiniz.

* Görevlileri gerektiğinde sizi uyarmadan sınavdan atabilir.

* Yanınızda sadece kağıt ve kalem taşımakta serbestsiniz. Kitap, defter, not ya da herhangi bir yardım sağlayacak araç gereci taşıyamazsınız. Bu sınavda yalnız başınızasınız.

# Kodlama Kuralları

* Kodunuzu C'de yazmalısınız.

* Faydalı fonksiyonlar ve dosyalar size subject dizininde verilecektir.

* Düzeltme tamamen otomatiktir, Deepthought ismini verdiğimiz bir program tarafından gerçekleştirilir.

* Eğer bir çalışma sizden bir veya birden fazla dosya ile program yazmanızı istiyorsa derlenme için şu komutlar  kullanılacaktır: clang -Wall -Wextra -Werror file1.c file2.c file3.c -o.

*  Eğer çalışma dosya isimlerini size bırakıyorsa, "clang -Wall -Wextra -Werror *.c -o program_name" formatında bir komut kullanınız.

* Son olarak, bir fonksiyon döndürmeniz gerektiğinde, clang -c -Wall -Wextra -Werror yourfile.c ile derleyebilirsiniz, sonrasında sistem kendi main fonksiyonunu da derleyip ikisini birleştirerek test için bir dosya oluşturur.

* İzin verilen fonksiyonlar çalışmaların başında belirtilecektir. İhtiyacınız olduğunu düşündüğünüz bir fonksiyonu kendiniz kodlayabilirsiniz. İzin verilmeyen bir fonksiyon kullanmak hile yapmak kategorisine girer, ve sonuç olarak tüm sınavdan kalırsınız, herhangi bir özel izin veya tartışma söz konusu olamaz. Unutmayın, uyarıldınız!

* Kullanabilmeniz için belirtilen fonksiyonlar dışındaki tüm fonksiyonlar kesinlikle yasaktır.
