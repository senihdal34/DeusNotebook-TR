#!/usr/bin/env python3
"""
Writes app/src/main/res/values{,-tr,-es,-zh,-pl}/strings_home.xml from the tables below.

Home, dialogs, snackbars, hints and the settings texts of the old upstream strings.xml (tr/es/zh only, pl has its own).
Edit a text here and run:  python3 scripts/gen_home_strings.py

Conventions: write a real newline for "\\n", plain quotes and apostrophes (they are escaped on output),
%1$s style placeholders, and "%%" for a literal percent sign in a string that is formatted with arguments.
A text with None for a language is skipped there (that language gets it from strings.xml, or falls back to English).
"""
import os
from xml.sax.saxutils import escape

RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'app', 'src', 'main', 'res')
LANGS = [('en', 'values'), ('tr', 'values-tr'), ('es', 'values-es'), ('zh', 'values-zh'), ('pl', 'values-pl')]

STRINGS = {}   # key -> {lang: text}
PLURALS = {}   # key -> {lang: {quantity: text}}


def S(key, en, tr, es, zh, pl):
    STRINGS[key] = dict(en=en, tr=tr, es=es, zh=zh, pl=pl)


def P(key, en, tr, es, zh, pl):
    PLURALS[key] = dict(en=en, tr=tr, es=es, zh=zh, pl=pl)


def U(key, tr, es, zh, pl_text=None):
    """An old upstream string that strings.xml already defines in English (and in Polish): translations for tr/es/zh."""
    S(key, None, tr, es, zh, pl_text)


# --------------------------------------------------------------------------------------------- common
S('action_cancel', 'Cancel', 'Vazgeç', 'Cancelar', '取消', 'Anuluj')
S('action_confirm', 'Confirm', 'Onayla', 'Confirmar', '确认', 'Potwierdź')
S('action_delete', 'Delete', 'Sil', 'Eliminar', '删除', 'Usuń')
S('action_add', 'Add', 'Ekle', 'Añadir', '添加', 'Dodaj')
S('not_implemented', 'Not implemented!', 'Henüz yapılmadı!', '¡Aún no está implementado!', '尚未实现！', 'Jeszcze niedostępne!')

# --------------------------------------------------------------------------------------------- main tabs
S('tab_planner', 'Planner', 'Planlayıcı', 'Planificador', '计划', 'Planer')
S('tab_notes', 'Notes', 'Notlar', 'Notas', '笔记', 'Notatki')
S('tab_favorites', '★ Favorites', '★ Favoriler', '★ Favoritos', '★ 收藏', '★ Ulubione')
S('tab_reading', 'Reading', 'Okuma', 'Lectura', '阅读', 'Czytanie')

# --------------------------------------------------------------------------------------------- Home
S('home_title_notes', 'Personal Notes', 'Kişisel Notlar', 'Notas personales', '个人笔记', 'Notatki osobiste')
S('home_title_favorites', 'Favorite Notes', 'Favori Notlar', 'Notas favoritas', '收藏的笔记', 'Ulubione notatki')
S('home_title_reading', 'Reading Board', 'Okuma Panosu', 'Panel de lectura', '阅读看板', 'Tablica czytania')
S('home_date_pattern', 'EEEE, d MMMM yyyy', 'EEEE, d MMMM yyyy', "EEEE, d 'de' MMMM 'de' yyyy", 'yyyy年M月d日 EEEE', 'EEEE, d MMMM yyyy')
S('home_summary', '%1$s · %2$s', '%1$s · %2$s', '%1$s · %2$s', '%1$s · %2$s', '%1$s · %2$s')
P('home_notes_count',
  {'one': '%1$d note', 'other': '%1$d notes'},
  {'one': '%1$d not', 'other': '%1$d not'},
  {'one': '%1$d nota', 'other': '%1$d notas'},
  {'other': '%1$d 条笔记'},
  {'one': '%1$d notatka', 'few': '%1$d notatki', 'many': '%1$d notatek', 'other': '%1$d notatki'})
P('home_favorites_count',
  {'one': '%1$d favorite', 'other': '%1$d favorites'},
  {'one': '%1$d favori', 'other': '%1$d favori'},
  {'one': '%1$d favorita', 'other': '%1$d favoritas'},
  {'other': '%1$d 个收藏'},
  {'one': '%1$d ulubiona', 'few': '%1$d ulubione', 'many': '%1$d ulubionych', 'other': '%1$d ulubione'})
S('home_settings', 'Settings', 'Ayarlar', 'Ajustes', '设置', 'Ustawienia')
S('home_favorites_label', 'Favorites', 'Sabit', 'Favoritas', '收藏', 'Ulubione')
S('home_no_favorites', 'No favorite notes yet. Press and hold a note card to add one.',
  'Sabit not yok. Bir notu sabitlemek için kartına basılı tut.',
  'Aún no hay notas favoritas. Mantén pulsada la tarjeta de una nota para añadirla.',
  '还没有收藏的笔记。长按笔记卡片即可收藏。',
  'Brak ulubionych notatek. Przytrzymaj kartę notatki, aby ją dodać.')
S('home_added_to_favorites', 'Added to favorites', 'Sabitlendi', 'Añadida a favoritos', '已加入收藏', 'Dodano do ulubionych')
S('home_removed_from_favorites', 'Removed from favorites', 'Sabitten kaldırıldı', 'Quitada de favoritos', '已取消收藏', 'Usunięto z ulubionych')
S('home_remove', 'Remove', 'Kaldır', 'Quitar', '移除', 'Usuń')
S('home_topics_all', 'All', 'Tümü', 'Todo', '全部', 'Wszystkie')
S('home_delete_topic_q', 'Delete topic?', 'Konu silinsin mi?', '¿Eliminar el tema?', '删除该主题？', 'Usunąć temat?')
S('home_delete_topic', 'Delete topic', 'Konuyu sil', 'Eliminar tema', '删除主题', 'Usuń temat')
S('home_delete_note_q', 'Delete note?', 'Not silinsin mi?', '¿Eliminar la nota?', '删除这条笔记？', 'Usunąć notatkę?')
S('home_delete_note', 'Delete note', 'Notu sil', 'Eliminar nota', '删除笔记', 'Usuń notatkę')
S('home_choose_tag_button', '# Choose', '# Seç', '# Elegir', '# 选择', '# Wybierz')
S('home_add_tag_button', '+ Tag', '+ Etiket', '+ Etiqueta', '+ 标签', '+ Etykieta')
S('home_new_topic_hint', 'new topic…', 'yeni konu…', 'nuevo tema…', '新主题…', 'nowy temat…')
S('home_new_tag_hint', 'new tag…', 'yeni etiket…', 'nueva etiqueta…', '新标签…', 'nowa etykieta…')
S('home_no_notes', 'No notes yet. Write your first one with the button below.',
  'Henüz not yok. Aşağıdaki düğmeyle ilk notunu yaz.',
  'Aún no hay notas. Escribe la primera con el botón de abajo.',
  '还没有笔记。点下面的按钮写第一条吧。',
  'Brak notatek. Napisz pierwszą przyciskiem poniżej.')
S('home_no_notes_in_topic', 'No notes in this topic. Write #%1$s inside a note and it shows up here.',
  'Bu konuda not yok. Notun içine #%1$s yazınca burada görünür.',
  'No hay notas en este tema. Escribe #%1$s dentro de una nota y aparecerá aquí.',
  '这个主题下还没有笔记。在笔记里写上 #%1$s，就会出现在这里。',
  'Brak notatek w tym temacie. Napisz #%1$s w notatce, a pojawi się tutaj.')
S('home_latest_note', 'Latest note', 'Son not', 'Última nota', '最新笔记', 'Ostatnia notatka')
S('home_one_page', '1 page', '1 sayfa', '1 página', '1 页', '1 strona')
S('home_topics', 'Topics', 'Konular', 'Temas', '主题', 'Tematy')
S('home_no_topics', 'No topics yet', 'Henüz konu yok', 'Aún no hay temas', '还没有主题', 'Brak tematów')
S('home_new_note', '+ New note', '+ Yeni not yaz', '+ Nueva nota', '+ 新建笔记', '+ Nowa notatka')
S('home_no_tags', 'No tags yet. Add the first one with “+ Tag”.',
  'Henüz etiket yok. “+ Etiket” ile ilkini ekle.',
  'Aún no hay etiquetas. Añade la primera con “+ Etiqueta”.',
  '还没有标签。点“+ 标签”添加第一个。',
  'Brak etykiet. Dodaj pierwszą przyciskiem „+ Etykieta”.')
S('home_choose_tag', 'Choose tag', 'Etiket seç', 'Elegir etiqueta', '选择标签', 'Wybierz etykietę')
S('home_untitled_note', 'Untitled note', 'İsimsiz Not', 'Nota sin título', '未命名笔记', 'Notatka bez tytułu')

# --------------------------------------------------------------------------------------------- how old a note is
S('rel_today', 'today', 'bugün', 'hoy', '今天', 'dzisiaj')
S('rel_yesterday', 'yesterday', 'dün', 'ayer', '昨天', 'wczoraj')
S('rel_ago', '%1$s ago', '%1$s önce', 'hace %1$s', '%1$s前', '%1$s temu')
S('rel_join', '%1$s %2$s', '%1$s %2$s', '%1$s %2$s', '%1$s%2$s', '%1$s %2$s')
P('rel_year',
  {'one': '%1$d year', 'other': '%1$d years'},
  {'one': '%1$d yıl', 'other': '%1$d yıl'},
  {'one': '%1$d año', 'other': '%1$d años'},
  {'other': '%1$d年'},
  {'one': '%1$d rok', 'few': '%1$d lata', 'many': '%1$d lat', 'other': '%1$d lat'})
P('rel_month',
  {'one': '%1$d month', 'other': '%1$d months'},
  {'one': '%1$d ay', 'other': '%1$d ay'},
  {'one': '%1$d mes', 'other': '%1$d meses'},
  {'other': '%1$d个月'},
  {'one': '%1$d miesiąc', 'few': '%1$d miesiące', 'many': '%1$d miesięcy', 'other': '%1$d miesiąca'})
P('rel_week',
  {'one': '%1$d week', 'other': '%1$d weeks'},
  {'one': '%1$d hafta', 'other': '%1$d hafta'},
  {'one': '%1$d semana', 'other': '%1$d semanas'},
  {'other': '%1$d周'},
  {'one': '%1$d tydzień', 'few': '%1$d tygodnie', 'many': '%1$d tygodni', 'other': '%1$d tygodnia'})
P('rel_day',
  {'one': '%1$d day', 'other': '%1$d days'},
  {'one': '%1$d gün', 'other': '%1$d gün'},
  {'one': '%1$d día', 'other': '%1$d días'},
  {'other': '%1$d天'},
  {'one': '%1$d dzień', 'few': '%1$d dni', 'many': '%1$d dni', 'other': '%1$d dnia'})

# --------------------------------------------------------------------------------------------- dialogs
S('dialog_confirm_deletion', 'Confirm Deletion', 'Silmeyi onayla', 'Confirmar eliminación', '确认删除', 'Potwierdź usunięcie')
S('dialog_delete_page_q', 'Are you sure you want to delete this page?',
  'Bu sayfayı silmek istediğine emin misin?', '¿Seguro que quieres eliminar esta página?',
  '确定要删除这一页吗？', 'Czy na pewno chcesz usunąć tę stronę?')
S('dialog_delete_notebook_q', 'Are you sure you want to delete "%1$s"?',
  '"%1$s" defterini silmek istediğine emin misin?', '¿Seguro que quieres eliminar "%1$s"?',
  '确定要删除“%1$s”吗？', 'Czy na pewno chcesz usunąć „%1$s”?')
S('empty_book_title', 'There is a book without pages!!!', 'Sayfası olmayan bir defter var!',
  '¡Hay un cuaderno sin páginas!', '有一个没有页面的笔记本！', 'Jest zeszyt bez stron!')
S('empty_book_message', 'We suggest deleting book "%1$s", it was created at %2$s. Do you want to do it?',
  '"%1$s" defterini silmeni öneririz; %2$s tarihinde oluşturulmuş. Silmek ister misin?',
  'Te sugerimos eliminar el cuaderno "%1$s", creado el %2$s. ¿Quieres hacerlo?',
  '建议删除笔记本“%1$s”（创建于 %2$s）。要删除吗？',
  'Proponujemy usunąć zeszyt „%1$s”, utworzony %2$s. Czy chcesz to zrobić?')
S('pdf_import_title', 'Import PDF Background', 'PDF arka planı içe aktar', 'Importar fondo PDF', '导入 PDF 背景', 'Importuj tło PDF')
S('pdf_import_question', 'Do you want to copy or observe the PDF?', 'PDF kopyalansın mı, yoksa izlensin mi?',
  '¿Quieres copiar u observar el PDF?', '要复制 PDF，还是监视原文件？', 'Skopiować PDF czy go obserwować?')
S('pdf_import_observe_label', '• Observe:', '• İzle:', '• Observar:', '• 监视：', '• Obserwuj:')
S('pdf_import_observe_text',
  'The app will link to the original file. This is useful for files that change often (e.g., from cloud services or LaTeX).',
  'Uygulama özgün dosyaya bağlanır. Sık değişen dosyalar için işe yarar (ör. bulut hizmetleri ya da LaTeX).',
  'La aplicación enlazará con el archivo original. Es útil para archivos que cambian a menudo (por ejemplo, de servicios en la nube o LaTeX).',
  '应用会链接到原始文件，适合经常变化的文件（例如来自云服务或 LaTeX）。',
  'Aplikacja połączy się z oryginalnym plikiem. To przydatne przy plikach, które często się zmieniają (np. z usług w chmurze lub LaTeX).')
S('pdf_import_path_warning',
  'Warning: The file path is very long (%1$d characters). Observing may fail on some systems.',
  'Uyarı: Dosya yolu çok uzun (%1$d karakter). İzleme bazı sistemlerde çalışmayabilir.',
  'Aviso: la ruta del archivo es muy larga (%1$d caracteres). Observar puede fallar en algunos sistemas.',
  '警告：文件路径很长（%1$d 个字符），在某些系统上监视可能失败。',
  'Uwaga: ścieżka pliku jest bardzo długa (%1$d znaków). Obserwowanie może nie działać na niektórych systemach.')
S('pdf_import_copy_label', '• Copy:', '• Kopyala:', '• Copiar:', '• 复制：', '• Kopiuj:')
S('pdf_import_copy_text',
  'The app will make its own copy of the file. Use this for safe, static storage.',
  'Uygulama dosyanın kendi kopyasını alır. Güvenli, değişmeyen bir saklama için bunu seç.',
  'La aplicación hará su propia copia del archivo. Úsalo para un almacenamiento seguro y estático.',
  '应用会保存一份自己的副本，适合安全、固定的存储。',
  'Aplikacja zrobi własną kopię pliku. Użyj tego do bezpiecznego, statycznego przechowywania.')
S('pdf_import_copy', 'Copy', 'Kopyala', 'Copiar', '复制', 'Kopiuj')
S('pdf_import_observe', 'Observe', 'İzle', 'Observar', '监视', 'Obserwuj')
S('export_dialog_title', 'Choose Export Format', 'Dışa aktarma biçimini seç', 'Elige el formato de exportación', '选择导出格式', 'Wybierz format eksportu')
S('export_dialog_body',
  'Select the format in which you want to export the book:\n- Xopp: Preserves all data and can be imported. However, if opened and saved by Xournal++, tool-specific information will be lost, and all strokes will be interpreted as ballpoint pen.\n- PDF: A standard format for document sharing.',
  'Defteri hangi biçimde dışa aktarmak istediğini seç:\n- Xopp: Tüm veriyi korur ve geri içe aktarılabilir. Ancak Xournal++ ile açıp kaydedersen araca özgü bilgiler kaybolur ve bütün çizgiler tükenmez kalem sayılır.\n- PDF: Belge paylaşımı için standart biçim.',
  'Elige el formato en el que quieres exportar el cuaderno:\n- Xopp: conserva todos los datos y se puede importar. Pero si Xournal++ lo abre y lo guarda, se pierde la información de cada herramienta y todos los trazos se interpretan como bolígrafo.\n- PDF: un formato estándar para compartir documentos.',
  '请选择导出笔记本的格式：\n- Xopp：保留全部数据，可重新导入。但如果用 Xournal++ 打开并保存，各工具的专有信息会丢失，所有笔画都会被当作圆珠笔。\n- PDF：通用的文档分享格式。',
  'Wybierz format, w którym chcesz wyeksportować zeszyt:\n- Xopp: zachowuje wszystkie dane i można go zaimportować z powrotem. Jednak po otwarciu i zapisaniu w Xournal++ tracone są informacje specyficzne dla narzędzi, a wszystkie pociągnięcia są traktowane jak długopis.\n- PDF: standardowy format do udostępniania dokumentów.')
S('export_as_pdf', 'Export as PDF', 'PDF olarak aktar', 'Exportar como PDF', '导出为 PDF', 'Eksportuj jako PDF')
S('export_as_xopp', 'Export as Xopp', 'Xopp olarak aktar', 'Exportar como Xopp', '导出为 Xopp', 'Eksportuj jako Xopp')
S('export_book_pdf_progress', 'Exporting book to PDF..', 'Defter PDF olarak aktarılıyor…', 'Exportando el cuaderno a PDF…', '正在将笔记本导出为 PDF…', 'Eksportowanie zeszytu do PDF…')
S('export_book_xopp_progress', 'Exporting the book to xopp...', 'Defter xopp olarak aktarılıyor…', 'Exportando el cuaderno a xopp…', '正在将笔记本导出为 xopp…', 'Eksportowanie zeszytu do xopp…')
S('folder_move_prompt', 'Choose folder to move "%1$s":', '"%1$s" için hedef klasörü seç:', 'Elige la carpeta a la que mover "%1$s":', '选择要把“%1$s”移到的文件夹：', 'Wybierz folder, do którego przenieść „%1$s”:')
S('folder_setting', 'Folder Setting', 'Klasör ayarı', 'Ajustes de la carpeta', '文件夹设置', 'Ustawienia folderu')
S('folder_title', 'Folder Title', 'Klasör adı', 'Nombre de la carpeta', '文件夹名称', 'Nazwa folderu')
S('folder_delete', 'Delete Folder', 'Klasörü sil', 'Eliminar carpeta', '删除文件夹', 'Usuń folder')
S('bg_type_observe_pdf', 'Observe Pdf', 'PDF\'yi izle', 'Observar PDF', '监视 PDF', 'Obserwuj PDF')
S('bg_type_cover_image', 'Cover Image', 'Kapak resmi', 'Imagen de portada', '封面图片', 'Obraz okładki')
S('bg_type_image', 'Image', 'Resim', 'Imagen', '图片', 'Obraz')
S('bg_type_repeating_image', 'Repeating Image', 'Tekrarlanan resim', 'Imagen repetida', '重复图片', 'Powtarzany obraz')
S('bg_type_native', 'Native', 'Hazır', 'Nativo', '内置', 'Natywny')
S('bg_type_static_pdf_page', 'Static pdf Page', 'Sabit PDF sayfası', 'Página PDF estática', '静态 PDF 页面', 'Statyczna strona PDF')
S('bg_choose_cover_image', 'Choose Cover Image', 'Kapak resmi seç', 'Elegir imagen de portada', '选择封面图片', 'Wybierz obraz okładki')
S('bg_choose_repeating_image', 'Choose Repeating Image', 'Tekrarlanan resmi seç', 'Elegir imagen repetida', '选择重复图片', 'Wybierz powtarzany obraz')
S('bg_choose_image', 'Choose Image', 'Resim seç', 'Elegir imagen', '选择图片', 'Wybierz obraz')
S('bg_choose_from_file', 'Choose From File...', 'Dosyadan seç…', 'Elegir de un archivo…', '从文件选择…', 'Wybierz z pliku…')
S('bg_import_pdf', 'Import PDF', 'PDF içe aktar', 'Importar PDF', '导入 PDF', 'Importuj PDF')
S('notebook_link_none', 'none', 'yok', 'ninguno', '无', 'brak')
S('notebook_link', 'Link', 'Bağla', 'Vincular', '链接', 'Połącz')
S('notebook_unlink', 'Unlink', 'Bağlantıyı kaldır', 'Desvincular', '取消链接', 'Odłącz')
S('page_move_left', 'Move Left', 'Sola taşı', 'Mover a la izquierda', '左移', 'Przesuń w lewo')
S('page_move_right', 'Move right', 'Sağa taşı', 'Mover a la derecha', '右移', 'Przesuń w prawo')
S('page_insert_after', 'Insert after', 'Sonrasına ekle', 'Insertar después', '在后面插入', 'Wstaw po')
S('page_duplicate', 'Duplicate', 'Çoğalt', 'Duplicar', '复制一份', 'Duplikuj')
S('quicknav_favorite_pages', 'Favorite pages', 'Favori sayfalar', 'Páginas favoritas', '收藏的页面', 'Ulubione strony')
S('pages_jump_to_current', 'Jump to current', 'Geçerli sayfaya git', 'Ir a la actual', '跳到当前页', 'Przejdź do bieżącej')
S('pages_edit_mode', 'Edit Mode', 'Düzenleme modu', 'Modo de edición', '编辑模式', 'Tryb edycji')
S('capture_new', 'New Capture', 'Yeni hızlı not', 'Nueva captura', '新建速记', 'Nowy zapis')
S('sync_in_progress', 'Syncing...', 'Eşitleniyor...', 'Sincronizando...', '同步中...', 'Synchronizacja...')

# --------------------------------------------------------------------------------------------- settings
S('settings_clearing', 'Clearing...', 'Temizleniyor...', 'Borrando...', '正在清除...', 'Czyszczenie...')
S('settings_delete_all_q', 'Delete all pages, notebooks, and folders?', 'Bütün sayfalar, defterler ve klasörler silinsin mi?',
  '¿Eliminar todas las páginas, cuadernos y carpetas?', '删除所有页面、笔记本和文件夹？', 'Usunąć wszystkie strony, zeszyty i foldery?')
S('settings_yes_delete_all', 'Yes, delete all', 'Evet, hepsini sil', 'Sí, eliminar todo', '是，全部删除', 'Tak, usuń wszystko')
S('settings_clear_all_pages', 'Clear all pages', 'Bütün sayfaları temizle', 'Borrar todas las páginas', '清除所有页面', 'Wyczyść wszystkie strony')
S('settings_capture_title', 'Capture', 'Hızlı not', 'Captura', '速记', 'Zapis')
S('settings_capture_description',
  'Handwritten captures are recognized and saved as markdown to your Obsidian vault. Tags are loaded from existing notes in this folder.',
  'El yazısı notlar tanınır ve Obsidian kasana markdown olarak kaydedilir. Etiketler bu klasördeki mevcut notlardan yüklenir.',
  'Las capturas escritas a mano se reconocen y se guardan como markdown en tu vault de Obsidian. Las etiquetas se cargan de las notas que ya hay en esta carpeta.',
  '手写速记会被识别，并以 Markdown 格式保存到你的 Obsidian 库。标签取自此文件夹中已有的笔记。',
  'Odręczne zapisy są rozpoznawane i zapisywane jako markdown w Twoim sejfie Obsidian. Etykiety są wczytywane z istniejących notatek w tym folderze.')
S('settings_vault_folder', 'Vault inbox folder', 'Kasa gelen kutusu klasörü', 'Carpeta de entrada del vault', '库的收件箱文件夹', 'Folder skrzynki odbiorczej sejfu')
S('settings_vault_folder_hint', 'Relative to /storage/emulated/0/. Press Done to save.',
  '/storage/emulated/0/ klasörüne göre. Kaydetmek için Bitti\'ye bas.',
  'Relativa a /storage/emulated/0/. Pulsa Hecho para guardar.',
  '相对于 /storage/emulated/0/。按“完成”保存。',
  'Względem /storage/emulated/0/. Naciśnij Gotowe, aby zapisać.')

# --------------------------------------------------------------------------------------------- bug report
S('report_title', 'Report an Issue', 'Sorun bildir', 'Informar de un problema', '报告问题', 'Zgłoś problem')
S('report_description_label', 'Issue description', 'Sorunun açıklaması', 'Descripción del problema', '问题描述', 'Opis problemu')
S('report_include_logs', 'Include diagnostic logs', 'Tanılama kayıtlarını ekle', 'Incluir registros de diagnóstico', '附上诊断日志', 'Dołącz dzienniki diagnostyczne')
S('report_logs_from', 'Include logs from:', 'Şu kayıtları ekle:', 'Incluir registros de:', '附上以下来源的日志：', 'Dołącz dzienniki z:')
S('report_include_libraries', 'Include libraries logs', 'Kütüphane kayıtlarını ekle', 'Incluir registros de las bibliotecas', '附上库的日志', 'Dołącz dzienniki bibliotek')
S('report_copy', 'Copy Report', 'Raporu kopyala', 'Copiar informe', '复制报告', 'Kopiuj raport')
S('report_submit', 'Submit via GitHub', 'GitHub üzerinden gönder', 'Enviar por GitHub', '通过 GitHub 提交', 'Wyślij przez GitHub')
S('report_preview', '📋 Report Preview', '📋 Rapor önizlemesi', '📋 Vista previa del informe', '📋 报告预览', '📋 Podgląd raportu')
S('report_submit_failed', 'Failed to submit report', 'Rapor gönderilemedi', 'No se pudo enviar el informe', '提交报告失败', 'Nie udało się wysłać raportu')
S('report_copied', 'Report copied to clipboard', 'Rapor panoya kopyalandı', 'Informe copiado al portapapeles', '报告已复制到剪贴板', 'Raport skopiowany do schowka')

# --------------------------------------------------------------------------------------------- snackbars and hints
S('snack_error', 'Error: %1$s', 'Hata: %1$s', 'Error: %1$s', '错误：%1$s', 'Błąd: %1$s')
S('snack_import_failed', 'Import failed: %1$s', 'İçe aktarma başarısız: %1$s', 'Error al importar: %1$s', '导入失败：%1$s', 'Import nie powiódł się: %1$s')
S('snack_pdf_importing_copy', 'Importing PDF background (copy)', 'PDF arka planı içe aktarılıyor (kopya)', 'Importando fondo PDF (copia)', '正在导入 PDF 背景（副本）', 'Importowanie tła PDF (kopia)')
S('snack_pdf_observer', 'Setting up observer for PDF', 'PDF için izleme kuruluyor', 'Configurando la observación del PDF', '正在为 PDF 设置监视', 'Konfigurowanie obserwowania PDF')
S('snack_pdf_import_ok', 'PDF Import Successful', 'PDF içe aktarıldı', 'PDF importado', 'PDF 导入成功', 'PDF zaimportowany')
S('snack_xopp_importing', 'Importing from xopp file...', 'xopp dosyasından içe aktarılıyor...', 'Importando desde un archivo xopp...', '正在从 xopp 文件导入...', 'Importowanie z pliku xopp...')
S('snack_xopp_import_ok', 'XOPP Import Successful', 'XOPP içe aktarıldı', 'XOPP importado', 'XOPP 导入成功', 'XOPP zaimportowany')
S('snack_quicknav_no_source', "Can't go back, no QuickNav source page", 'Geri dönülemiyor: Hızlı gezinmenin çıkış sayfası yok',
  'No se puede volver: no hay página de origen de QuickNav', '无法返回：没有快速导航的来源页面', 'Nie można wrócić: brak strony źródłowej QuickNav')
S('snack_sync_failed', 'Sync failed: %1$s', 'Eşitleme başarısız: %1$s', 'Error de sincronización: %1$s', '同步失败：%1$s', 'Synchronizacja nie powiodła się: %1$s')
S('snack_bg_missing', 'Background does not exist', 'Arka plan dosyası yok', 'El fondo no existe', '背景文件不存在', 'Tło nie istnieje')
S('snack_bg_changed', 'Background file changed', 'Arka plan dosyası değişti', 'El archivo de fondo cambió', '背景文件已更改', 'Plik tła został zmieniony')
S('snack_page_not_found', 'Could not find page, cleaning book', 'Sayfa bulunamadı, defter temizleniyor', 'No se encontró la página, limpiando el cuaderno', '找不到该页，正在清理笔记本', 'Nie znaleziono strony, czyszczenie zeszytu')
S('snack_page_too_large', 'Page is too large!', 'Sayfa çok büyük!', '¡La página es demasiado grande!', '页面太大！', 'Strona jest zbyt duża!')
S('snack_nothing_selected', "There isn't anything.", 'Burada hiçbir şey yok.', 'No hay nada.', '这里什么都没有。', 'Nic tu nie ma.')
S('snack_page_empty', 'Page is empty!', 'Sayfa boş!', '¡La página está vacía!', '页面是空的！', 'Strona jest pusta!')
S('snack_nothing_to_undo', 'Nothing to undo/redo', 'Geri alınacak ya da yinelenecek bir şey yok', 'Nada que deshacer o rehacer', '没有可撤销或重做的内容', 'Nic do cofnięcia ani ponowienia')
S('snack_loading_strokes', 'Loading strokes...', 'Çizgiler yükleniyor...', 'Cargando trazos...', '正在加载笔迹...', 'Wczytywanie pociągnięć...')
S('snack_waiting_drawing', 'Waiting for drawing to finish…', 'Çizimin bitmesi bekleniyor…', 'Esperando a que termine el dibujo…', '正在等待绘制完成…', 'Czekam na zakończenie rysowania…')
S('snack_no_file_permission', 'No file permissions! Please grant file permissions and restart the app',
  'Dosya izni yok! Lütfen dosya izni ver ve uygulamayı yeniden başlat',
  '¡Sin permiso de archivos! Concede el permiso y reinicia la aplicación',
  '没有文件权限！请授予文件权限并重启应用', 'Brak uprawnień do plików! Przyznaj uprawnienia i uruchom aplikację ponownie')
S('snack_migration_complete', 'Stroke migration complete.', 'Çizgi dönüşümü tamamlandı.', 'Migración de trazos completada.', '笔迹迁移完成。', 'Migracja pociągnięć zakończona.')
S('snack_migrating', 'Migrating strokes: %1$s%% (%2$d/%3$d) batch=%4$d', 'Çizgiler dönüştürülüyor: %1$s%% (%2$d/%3$d) küme=%4$d',
  'Migrando trazos: %1$s%% (%2$d/%3$d) lote=%4$d', '正在迁移笔迹：%1$s%%（%2$d/%3$d）批次=%4$d', 'Migracja pociągnięć: %1$s%% (%2$d/%3$d) partia=%4$d')
S('snack_migration_deleted_oversize', 'Deleted oversized stroke data during migration. Some pen strokes may have been removed.',
  'Dönüşüm sırasında çok büyük çizgi verileri silindi. Bazı kalem çizgileri kaybolmuş olabilir.',
  'Se eliminaron datos de trazos demasiado grandes durante la migración. Puede que falten algunos trazos.',
  '迁移时删除了过大的笔迹数据，部分笔画可能已丢失。',
  'Podczas migracji usunięto zbyt duże dane pociągnięć. Niektóre pociągnięcia mogły zniknąć.')
S('hint_selection_mode', 'Selection mode!', 'Seçim modu!', '¡Modo de selección!', '选择模式！', 'Tryb zaznaczania!')
S('hint_drag_mode', 'Drag mode!', 'Sürükleme modu!', '¡Modo de arrastre!', '拖动模式！', 'Tryb przeciągania!')
S('hint_cut_to_clipboard', 'Content cut to clipboard', 'İçerik panoya kesildi', 'Contenido cortado al portapapeles', '内容已剪切到剪贴板', 'Zawartość wycięta do schowka')
S('hint_pasted', 'Pasted content from clipboard', 'Pano içeriği yapıştırıldı', 'Contenido pegado desde el portapapeles', '已从剪贴板粘贴内容', 'Wklejono zawartość ze schowka')
S('hint_strokes_no_resize', 'For now, strokes cannot be resized', 'Çizgiler şimdilik yeniden boyutlandırılamıyor', 'Por ahora los trazos no se pueden redimensionar', '目前无法调整笔迹大小', 'Na razie nie można zmieniać rozmiaru pociągnięć')
S('hint_image_error', 'There was an error during image processing.', 'Resim işlenirken bir hata oluştu.', 'Hubo un error al procesar la imagen.', '处理图片时出错。', 'Wystąpił błąd podczas przetwarzania obrazu.')
S('hint_eraser', 'Eraser', 'Silgi', 'Borrador', '橡皮擦', 'Gumka')
S('hint_pen', 'Pen', 'Kalem', 'Lápiz', '笔', 'Pióro')
S('hint_image_load_failed', 'Image cannot be loaded.', 'Resim yüklenemedi.', 'No se puede cargar la imagen.', '无法加载图片。', 'Nie można wczytać obrazu.')
S('hint_image_permission', 'Permission error: Unable to access image.', 'İzin hatası: Resme erişilemiyor.', 'Error de permisos: no se puede acceder a la imagen.', '权限错误：无法访问图片。', 'Błąd uprawnień: brak dostępu do obrazu.')
S('hint_images_load_failed', 'Failed to load images.', 'Resimler yüklenemedi.', 'No se pudieron cargar las imágenes.', '无法加载图片。', 'Nie udało się wczytać obrazów.')
S('hint_strokes_draw_failed', 'Error drawing strokes', 'Çizgiler çizilirken hata oluştu', 'Error al dibujar los trazos', '绘制笔迹时出错', 'Błąd podczas rysowania pociągnięć')
S('update_preview_available', 'A newer preview version is available!\nYou are using released %1$s, and newest is from %2$s.',
  'Daha yeni bir önizleme sürümü var!\nYayımlanmış %1$s sürümünü kullanıyorsun, en yenisi %2$s.',
  '¡Hay una versión de vista previa más reciente!\nUsas la versión publicada %1$s y la más nueva es de %2$s.',
  '有更新的预览版！\n你使用的是正式版 %1$s，最新版本为 %2$s。',
  'Dostępna jest nowsza wersja zapoznawcza!\nUżywasz wydanej wersji %1$s, a najnowsza jest z %2$s.')
S('update_stable_available', 'A newer stable version is available!\nYou are using %1$s, while the latest is %2$s.',
  'Daha yeni bir kararlı sürüm var!\n%1$s sürümünü kullanıyorsun, en yenisi %2$s.',
  '¡Hay una versión estable más reciente!\nUsas la %1$s y la última es la %2$s.',
  '有更新的稳定版！\n你使用的是 %1$s，最新版本为 %2$s。',
  'Dostępna jest nowsza wersja stabilna!\nUżywasz %1$s, a najnowsza to %2$s.')

# --------------------------------------------------------------------------------------------- capture page toolbar
S('inbox_back', '← Back', '← Geri', '← Atrás', '← 返回', '← Wstecz')
S('inbox_capture', 'Capture', 'Hızlı not', 'Captura', '速记', 'Zapis')
P('inbox_capture_tags',
  {'one': 'Capture · %1$d tag', 'other': 'Capture · %1$d tags'},
  {'one': 'Hızlı not · %1$d etiket', 'other': 'Hızlı not · %1$d etiket'},
  {'one': 'Captura · %1$d etiqueta', 'other': 'Captura · %1$d etiquetas'},
  {'other': '速记 · %1$d 个标签'},
  {'one': 'Zapis · %1$d etykieta', 'few': 'Zapis · %1$d etykiety', 'many': 'Zapis · %1$d etykiet', 'other': 'Zapis · %1$d etykiety'})
S('inbox_save_exit', 'Save & Exit', 'Kaydet ve çık', 'Guardar y salir', '保存并退出', 'Zapisz i wyjdź')
S('inbox_tag_hint', 'search or add tags...', 'etiket ara ya da ekle...', 'buscar o añadir etiquetas...', '搜索或添加标签...', 'szukaj lub dodaj etykiety...')

# --------------------------------------------------------------------------------------------- old upstream strings.xml
# These keys exist in values/strings.xml (English) and, apart from the last three, in values-pl/strings.xml.
# Turkish, Spanish and Chinese had no translation of them: they are added here.
U('home_quick_pages', 'Hızlı sayfalar', 'Páginas rápidas', '快速页面')
U('home_notebooks', 'Defterler', 'Cuadernos', '笔记本')
U('home_add_new_folder', 'Yeni klasör ekle', 'Añadir carpeta nueva', '添加新文件夹')
U('home_new_folder', 'Yeni klasör', 'Nueva carpeta', '新文件夹')
U('home_view_name', 'Kitaplık', 'Biblioteca', '资料库')
U('settings_title', 'Ayarlar', 'Ajustes', '设置')
U('settings_tab_general_name', 'Genel', 'General', '常规')
U('settings_tab_gestures_name', 'Hareketler', 'Gestos', '手势')
U('default_page_background_template', 'Varsayılan sayfa arka plan şablonu', 'Plantilla de fondo de página predeterminada', '默认页面背景模板')
U('blank_page', 'Boş sayfa', 'Página en blanco', '空白页')
U('dot_grid', 'Noktalı', 'Cuadrícula de puntos', '点阵')
U('lines', 'Çizgili', 'Líneas', '横线')
U('small_squares_grid', 'Kareli', 'Cuadrícula de cuadros pequeños', '小方格')
U('hexagon_grid', 'Altıgen ızgara', 'Cuadrícula hexagonal', '六边形网格')
U('use_onyx_neotools_may_cause_crashes', 'Onyx NeoTools kullan (çökmelere yol açabilir)', 'Usar Onyx NeoTools (puede causar fallos)', '使用 Onyx NeoTools（可能导致崩溃）')
U('enable_scribble_to_erase', 'Karalayarak silmeyi aç (hatalarını karalayıp sil)', 'Activar borrar garabateando (tacha tus errores para borrarlos)', '启用涂抹擦除（把写错的地方涂掉即可擦除）')
U('enable_smooth_scrolling', 'Akıcı kaydırmayı aç', 'Activar desplazamiento suave', '启用平滑滚动')
U('continuous_zoom', 'Sürekli yakınlaştırma', 'Zoom continuo', '连续缩放')
U('continuous_stroke_slider', 'Sürekli çizgi kalınlığı kaydırıcısı', 'Control deslizante de trazo continuo', '连续笔画粗细滑块')
U('monochrome_mode', 'Tek renkli mod', 'Modo monocromo', '单色模式')
U('paginate_pdf', 'PDF\'yi sayfalara böl', 'Paginar PDF', 'PDF 分页')
U('preview_pdf_pagination', 'PDF sayfa bölünmesini önizle', 'Vista previa de la paginación del PDF', '预览 PDF 分页')
U('app_new_version', 'DeusNote\'un yeni bir sürümü GitHub\'da yayınlanmış gibi görünüyor!', 'Parece que hay una nueva versión de DeusNote en GitHub.', '看起来 GitHub 上有 DeusNote 的新版本！')
U('app_see_release', 'Sürümü tarayıcıda gör', 'Ver la versión en el navegador', '在浏览器中查看发布页')
U('app_latest_version', 'En son sürümü kullanıyorsun.', 'Tienes la última versión.', '你使用的已是最新版本。')
U('app_check_updates', 'Yeni sürümü denetle', 'Buscar una versión nueva', '检查新版本')
U('gestures_double_tap_action', 'Çift dokunma eylemi', 'Acción de doble toque', '双击操作')
U('gestures_two_finger_tap_action', 'İki parmakla dokunma eylemi', 'Acción de toque con dos dedos', '双指轻点操作')
U('gestures_swipe_left_action', 'Sola kaydırma eylemi', 'Acción de deslizar a la izquierda', '向左滑动操作')
U('gestures_swipe_right_action', 'Sağa kaydırma eylemi', 'Acción de deslizar a la derecha', '向右滑动操作')
U('gestures_two_finger_swipe_left_action', 'İki parmakla sola kaydırma eylemi', 'Acción de deslizar con dos dedos a la izquierda', '双指向左滑动操作')
U('gestures_two_finger_swipe_right_action', 'İki parmakla sağa kaydırma eylemi', 'Acción de deslizar con dos dedos a la derecha', '双指向右滑动操作')
S('start_in_planner', None, 'Uygulama açılınca haftalık planlayıcıyı aç', 'Abrir el planificador semanal al iniciar la aplicación', '启动应用时打开每周计划', 'Otwieraj planer tygodniowy po uruchomieniu aplikacji')
S('palm_guard', None, 'Avuç içi koruması: yazarken ve alt kenarda parmak hareketlerini yok say', 'Protección de palma: ignorar gestos de dedos al escribir y en el borde inferior', '防误触：书写时和屏幕下边缘忽略手指手势', 'Ochrona dłoni: ignoruj gesty palców podczas pisania i przy dolnej krawędzi')
S('pen_button_toggle', None, 'Kalemin yan düğmesi kalem ile silgi arasında geçiş yapar', 'El botón lateral del lápiz alterna entre lápiz y borrador', '笔侧键在书写和橡皮擦之间切换', 'Przycisk boczny pióra przełącza między piórem a gumką')
U('enable_quick_nav', 'Hızlı gezinmeyi açmak için üç parmakla dokun', 'Toca con tres dedos para abrir QuickNav', '三指触摸打开快速导航')
U('work_in_progress', '(devam ediyor)', '(en desarrollo)', '（开发中）')
U('toolbar_position_top', 'Üst', 'Arriba', '顶部')
U('toolbar_position_bottom', 'Alt', 'Abajo', '底部')
U('sponsor_button_text', 'Destek ol', 'Patrocinar', '赞助')
U('gesture_action_undo', 'Geri al', 'Deshacer', '撤销')
U('gesture_action_redo', 'Yinele', 'Rehacer', '重做')
U('gesture_action_previous_page', 'Önceki sayfa', 'Página anterior', '上一页')
U('gesture_action_next_page', 'Sonraki sayfa', 'Página siguiente', '下一页')
U('gesture_action_toggle_pen_eraser', 'Kalem / silgi geçişi', 'Alternar lápiz / borrador', '切换笔 / 橡皮')
U('gesture_action_toggle_zen_mode', 'Zen modunu aç/kapat', 'Alternar modo zen', '切换专注模式')
U('gesture_action_select', 'Seç', 'Seleccionar', '选择')
U('details_notebook_title', 'Başlık:', 'Título:', '标题：')
U('details_notebook_default_background_template', 'Varsayılan arka plan şablonu', 'Plantilla de fondo predeterminada', '默认背景模板')
U('details_notebook_pages', 'Sayfa: %1$d', 'Páginas: %1$d', '页数：%1$d')
U('details_notebook_in_folder', 'Klasör: ', 'En la carpeta: ', '所在文件夹：')
U('details_notebook_created', 'Oluşturulma: %1$s', 'Creado: %1$s', '创建时间：%1$s')
U('details_notebook_last_updated', 'Son güncelleme: %1$s', 'Última actualización: %1$s', '最后更新：%1$s')
U('details_notebook_buttons_delete', 'Sil', 'Eliminar', '删除')
U('details_notebook_buttons_move', 'Taşı', 'Mover', '移动')
U('details_notebook_buttons_export', 'Dışa aktar', 'Exportar', '导出')
U('details_notebook_buttons_copy', 'Kopyala', 'Copiar', '复制')
U('details_notebook_linked_to', 'Bağlı: %1$s', 'Vinculado a: %1$s', '已链接到：%1$s')
U('welcome_view_title', 'DeusNote\'a hoş geldin', 'Te damos la bienvenida a DeusNote', '欢迎使用 DeusNote')
U('welcome_view_subtitle', 'En iyi deneyim için şu kurulum adımlarını tamamla:', 'Para una experiencia óptima, completa estos pasos de configuración:', '为获得最佳体验，请完成以下设置步骤：')
U('welcome_view_file_access', 'Dosya erişimi', 'Acceso a archivos', '文件访问')
U('welcome_view_file_access_explanation', 'Notlarını kaydetmek ve açmak için gerekli', 'Necesario para guardar y cargar tus notas', '保存和读取笔记所必需')
U('welcome_view_refresh_mode', 'Önerilen yenileme modunu ayarla', 'Ajustar el modo de actualización recomendado', '设置推荐的刷新模式')
U('welcome_view_refresh_mode_details', 'HD modu ya da Regal modu önerilir', 'Se recomienda el modo HD o el modo Regal', '建议使用 HD 模式或 Regal 模式')
U('welcome_view_refresh_mode_applied', 'Uygulandı (%1$s)', 'Aplicado (%1$s)', '已应用（%1$s）')
U('welcome_view_refresh_mode_set_hd_mode', 'HD modunu ayarla (şu an %1$s)', 'Activar modo HD (ahora en %1$s)', '设为 HD 模式（当前为 %1$s）')
U('welcome_view_permissions_granted', 'Verildi ✓', 'Concedido ✓', '已授权 ✓')
U('welcome_view_permissions_button', 'İzin ver', 'Conceder permiso', '授予权限')
U('welcome_view_continue', 'Devam', 'Continuar', '继续')
U('welcome_view_complete_setup_first', 'Önce kurulumu tamamla', 'Completa primero la configuración', '请先完成设置')
U('welcome_view_prevent_frozen', '⚠️ DeusNote\'un dondurulmasını önle (Onyx cihazlar)', '⚠️ Evita que DeusNote se congele (dispositivos Onyx)', '⚠️ 防止 DeusNote 被冻结（Onyx 设备）')
U('welcome_view_prevent_frozen_details',
  'Onyx cihazlar pil tasarrufu için arka plandaki uygulamaları otomatik olarak dondurabilir (kapatabilir). Bu özelliği kapatmazsan DeusNote arka planda sürekli kapanır; bu hem can sıkar hem de iş kaybına ya da kesintilere yol açabilir. ',
  'Los dispositivos Onyx pueden congelar (cerrar) automáticamente las aplicaciones en segundo plano para ahorrar batería. Si no desactivas esta función, DeusNote se cerrará constantemente en segundo plano, lo que resulta molesto y puede causar pérdida de trabajo o interrupciones. ',
  'Onyx 设备可能会自动冻结（关闭）后台应用以节省电量。如果不关闭这一功能，DeusNote 在后台会不断被关闭，既烦人，还可能导致工作丢失或被打断。 ')
U('welcome_view_prevent_frozen_instructions_title', 'Dondurmayı nasıl önlersin:', 'Cómo evitar que se congele:', '如何防止被冻结：')
U('welcome_view_prevent_frozen_instructions',
  '1. Onyx başlatıcıda (ana ekran) DeusNote simgesine uzun bas.\n2. Menüden "Unfreeze app" seçeneğini seç.',
  '1. Mantén pulsado el icono de DeusNote en el lanzador de Onyx (pantalla de inicio).\n2. Elige "Unfreeze app" en el menú.',
  '1. 在 Onyx 启动器（主屏幕）上长按 DeusNote 图标。\n2. 在菜单中选择“Unfreeze app”。')
U('welcome_view_prevent_frozen_recommended', 'Sorunsuz bir deneyim için bu adım şiddetle önerilir.', 'Este paso es muy recomendable para una experiencia fluida.', '为保证流畅体验，强烈建议完成这一步。')
U('welcome_view_quick_start_title', '📖 Hızlı başlangıç ve hareket rehberi', '📖 Guía de inicio rápido y gestos', '📖 快速入门与手势指南')
U('welcome_view_quick_start_navigation', 'Gezinme', 'Navegación', '导航')
U('welcome_view_quick_start_navigation_details',
  '• Yukarı/aşağı kaydır: Sayfayı kaydır\n• Sola/sağa kaydır: Önceki/sonraki sayfa\n• İki parmakla çimdikle: Yakınlaştır\n• Sayfa numarasına dokun: Hızlı atla\n• İki parmakla sola/sağa kaydır: Araç çubuğunu göster/gizle',
  '• Deslizar arriba/abajo: desplazar la página\n• Deslizar a izquierda/derecha: página anterior/siguiente\n• Pellizcar con 2 dedos: zoom\n• Tocar el número de página: salto rápido\n• Deslizar con dos dedos a izquierda/derecha: mostrar/ocultar la barra de herramientas',
  '• 上下滑动：滚动页面\n• 左右滑动：上一页/下一页\n• 双指捏合：缩放\n• 点按页码：快速跳转\n• 双指左右滑动：显示/隐藏工具栏')
U('welcome_view_quick_start_selection_editing_title', 'Seçme ve düzenleme', 'Selección y edición', '选择与编辑')
U('welcome_view_quick_start_selection_editing_details',
  '• Basılı tutup sürükle: Öğeleri seç\n• Çift dokunma: Geri al\n• Seçime çift dokunma: Kopyala\n• Seçimi sürükle: Taşı\n• Karalayarak sil (açıksa)',
  '• Mantener y arrastrar: seleccionar elementos\n• Doble toque: deshacer\n• Doble toque sobre la selección: copiar\n• Arrastrar la selección: mover\n• Garabatear para borrar (si está activado)',
  '• 按住并拖动：选择内容\n• 双击：撤销\n• 双击所选内容：复制\n• 拖动所选内容：移动\n• 涂抹擦除（如已启用）')
U('welcome_view_quick_start_tips_title', 'İpuçları', 'Consejos', '小提示')
U('welcome_view_quick_start_tips_details',
  '• Görselleri hızla paylaşmak için \'Seçimi dışa aktar\'ı kullan.\n• Sayfalar arasında hızlı atlamak için sayfa numarasına dokun.\n• Doğal silme için Ayarlar\'dan \'Karalayarak silme\'yi aç.\n• Geri almak için çift dokun; bir seçimde çift dokunursan kopyalar.\n• DeusNote\'u LaTeX için canlı PDF görüntüleyici olarak kullanabilirsin (README\'ye bak).\n• Hareket eylemlerini Ayarlar\'dan özelleştirebilirsin.',
  '• Usa \'Exportar selección\' para compartir imágenes rápidamente.\n• Toca el número de página para saltar rápidamente entre páginas.\n• Activa \'Borrar garabateando\' en Ajustes para borrar de forma natural.\n• Doble toque para deshacer, o sobre una selección para copiarla.\n• Puedes usar DeusNote como visor de PDF en vivo para LaTeX (consulta el README).\n• Puedes personalizar las acciones de los gestos en Ajustes.',
  '• 用“导出所选内容”快速分享图片。\n• 点按页码可在页面之间快速跳转。\n• 在设置中开启“涂抹擦除”，擦除更自然。\n• 双击可撤销；双击所选内容可复制。\n• DeusNote 可作为 LaTeX 的实时 PDF 查看器（见 README）。\n• 可以在设置中自定义手势操作。')
U('export_page_to', 'Sayfayı dışa aktar: %1$s', 'Exportar página a %1$s', '将页面导出到 %1$s')
U('exporting_the_page_to', 'Sayfa dışa aktarılıyor: %1$s…', 'Exportando la página a %1$s…', '正在将页面导出到 %1$s…')
U('export_book_to', 'Defteri dışa aktar: %1$s', 'Exportar cuaderno a %1$s', '将笔记本导出到 %1$s')
U('exporting_the_book_to', 'Defter dışa aktarılıyor: %1$s…', 'Exportando el cuaderno a %1$s…', '正在将笔记本导出到 %1$s…')
U('clean_all_strokes', 'Bütün çizgileri temizle', 'Borrar todos los trazos', '清除所有笔迹')
U('cleared_all_strokes', 'Bütün çizgiler temizlendi', 'Se borraron todos los trazos', '已清除所有笔迹')
U('change_background', 'Arka planı değiştir', 'Cambiar fondo', '更换背景')
U('bug_report', 'Hata bildir', 'Informar de un error', '报告问题')
U('choose_pdf_background', 'PDF arka planı seç', 'Elegir fondo PDF', '选择 PDF 背景')
U('repeat_background', 'Arka planı tekrarla', 'Repetir fondo', '重复背景')
U('choose_native_template', 'Hazır şablon seç', 'Elegir plantilla nativa', '选择内置模板')
U('select_pdf_page', 'PDF sayfası seç', 'Seleccionar página del PDF', '选择 PDF 页面')
U('page_number', 'Sayfa numarası', 'Número de página', '页码')
U('observe_pdf', 'PDF\'yi izle', 'Observar PDF', '监视 PDF')
U('current_page', 'Geçerli sayfa', 'Página actual', '当前页')
U('toolbar_scribble_to_erase_two_lined_short', 'Karalayıp\nSil', 'Garabatear\npara borrar', '涂抹\n擦除')
U('toolbar_position', 'Araç çubuğu konumu', 'Posición de la barra de herramientas', '工具栏位置')
P('pdf_has_pages',
  None,
  {'other': 'PDF %1$d sayfa'},
  {'one': 'El PDF tiene %1$d página', 'other': 'El PDF tiene %1$d páginas'},
  {'other': 'PDF 共 %1$d 页'},
  None)


# --------------------------------------------------------------------------------------------- writer
def esc(text):
    t = escape(text).replace("'", "\\'").replace('"', '\\"').replace('\n', '\\n')
    if text != text.strip():
        t = '"' + t + '"'   # a quoted resource keeps its leading/trailing space
    return t


def write(lang, folder):
    lines = ['<?xml version="1.0" encoding="utf-8"?>', '<resources>']
    for key, per in STRINGS.items():
        text = per.get(lang)
        if text is None:
            continue
        lines.append(f'    <string name="{key}">{esc(text)}</string>')
    for key, per in PLURALS.items():
        items = per.get(lang)
        if items is None:
            continue
        lines.append(f'    <plurals name="{key}">')
        for q in ('zero', 'one', 'two', 'few', 'many', 'other'):
            if q in items:
                lines.append(f'        <item quantity="{q}">{esc(items[q])}</item>')
        lines.append('    </plurals>')
    lines.append('</resources>')
    d = os.path.join(RES, folder)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'strings_home.xml'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    for lang, folder in LANGS:
        write(lang, folder)
    new_en = sum(1 for v in STRINGS.values() if v['en'] is not None) + sum(1 for v in PLURALS.values() if v['en'] is not None)
    print('keys:', len(STRINGS), 'strings +', len(PLURALS), 'plurals;', new_en, 'new English keys')
