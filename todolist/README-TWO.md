# Muhammad Naufal Zaky Alsar

# 2106752041

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

Synchronous programming adalah programming yang dimana prosesnya ditunggu selesai dulu sebelum bisa mengeksekusi proses lainnya. 
Sedangkan asynchronous programming adalah programming yang dimana prosesnya tidak harus selesai dulu untuk menjalankan proses setelahnya.
Asynchronous programming tidak terikat pada suatu proses jadi proses bisa jalan terus-menerus tanpa menunggu proses yang lainnya terbalik dengan synchronous dimana prosesnya harus selesai terlebih dahulu sebelum bisa memulai proses baru.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini

Event-Driven Programming adalah programming yang dimana flow suatu program ditentukan dengan suatu event. Contoh penggunaanya pada tugas kali ini adalah saat menambahkan task.
Task baru ditambahkan saat user memulai suatu event yaitu menambahkan task (dengan memencet tombol add task dan mengisi formnya).

## Jelaskan penerapan asynchronous programming pada AJAX.

Browser pertama-tama akan membuat object XMLHttpRequest dan mengirimkan HttpRequest. 
Setelah itu server akan memproses HttpRequest dan server akan membuat respons dan mengirimkan data balik lagi ke browser.
Data yang dikirimkan server akan diproses oleh server menggunakan javascript dengan asinkronus dan ditampilkan ke pengguna.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

Pertama-tama saya membuat dua fungsi dibawah ini di views.py :

```

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
@login_required(login_url='/todolist/login/')
def tambahin(request):
    context = {}
    if request.method == "POST":
        temp = ToDoList(user=request.user, title=request.POST.get('todo'), description=request.POST.get('description'))
        temp.save()
        return redirect('todolist:show')
    return JsonResponse({'message': 'success'})

```

Tambahin berguna untuk menambah task sedangkan show_json untuk mengembalikan data json dengan filter user.

Setelah itu saya membuat routing di urls.py untuk add :

```

path('add/', tambahin, name='add'),

```

Agar bisa menambahkan task

Terakhir saya membuat script ini :

```

function update(){
        $.ajax({
          url: "/todolist/add/",
          method: "POST",
          headers: {
            "X-CSRFToken": getCookie("csrftoken")
          },
          data:{
            todo : $('#todo').val(),
            description : $("#description").val(),
          },
        success: function(){
          show();
        },
        error: function(){
          aler("error");
        }
      })}
      
      
function show() {
      $.get("/todolist/json", function(data) {
        $("#card").html("")
            for(let i = 0; i < data.length ; i++){
              let d = new Date(data[i].fields.date.substring(0,10));
             const date = d.toDateString()
                    $("#card").append(`<div class="card m-2" style="width: 18rem;">
        <div class="card-header" id="title">
        <h5 class="card-title">${data[i].fields.title}</h5>
        </div>
        <div class="card-body" id="title">
        <ul class="list-group list-group-flush">
        <li class="list-group-item">${data[i].fields.description}</li>
        <li class="list-group-item">Tanggal : ${date}</li>
        </ul>
        </div>
        <div class="card-body">
                <a class="btn btn-outline-danger" id="delete" onclick="deleteTask(${data[i].pk})">Delete</a>
            </div>`)
              }
          });
    }
    
    $(document).ready(function(){
          show();
      });
      
      function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

```

Show berguna untuk menampilkan html
Document ready agar pas pertama kali web diload maka akan dimenampilkan terlebih dahulu.
Update berguna untuk menambah task.
Getcookie berguna untuk proteksi dengan csrf





