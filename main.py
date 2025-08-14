import os
import json
import zipfile
import shutil
import datetime
from pathlib import Path

# Версия программы
PROGRAM_VERSION = "1.2"

# Настройки путей
BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / "config.json"
BIOMES_DIR = BASE_DIR / "biomes"
OVERLAYS_DIR = BASE_DIR / "overlays"
ALL_OVERLAY_DIR = OVERLAYS_DIR / "all"
EXPORT_DIR = BASE_DIR / "export"
BACKUPS_DIR = BASE_DIR / "backups"
GROUPS_DIR = BASE_DIR / "groups"

# Поддержка языков
LANGUAGES = {
    "en": {
        "welcome": f"Biome Processor Tool v{PROGRAM_VERSION}",
        "select_lang": "Select language (en/ru/zh): ",
        "invalid_lang": "Invalid language. Keeping current language.",
        "processing": "Processing biome: {}",
        "overlay_not_found": "Overlay not found for: {}",
        "biome_not_found": "Original biome not found: {}",
        "success": "Successfully processed {} biomes!",
        "biomes_missing": "No biomes found in {}",
        "downloading": "Downloading biomes from Minecraft...",
        "enter_version": "Enter Minecraft version (e.g. 1.21.8): ",
        "download_success": "Biomes downloaded successfully!",
        "download_failed": "Failed to download biomes. Please copy manually.",
        "global_overlay_applied": "Global overlay applied to {} overlays",
        "empty_overlays_created": "Created {} empty overlay templates",
        "menu": "\nMain Menu:\n1. Process biomes\n2. Apply global overlay\n3. Download biomes from .jar\n4. Create empty overlays\n5. Change language\n6. Show information\n7. Delete biomes by group\n8. Create group\n9. Exit\nSelect option: ",
        "invalid_option": "Invalid option!",
        "current_lang": "Current language: {}",
        "lang_changed": "Language changed to {}",
        "global_overlay_missing": "Global overlay not found at: {}",
        "no_overlays": "No overlays found in {}",
        "no_biomes": "No biomes found in {}",
        "goodbye": "Goodbye!",
        "first_run": "Welcome! Please select language",
        "version_info": "Program version: {}\nBiomes version: {}",
        "no_biomes_version": "Not downloaded",
        "delete_confirm": "Are you sure you want to delete {} biomes? (y/n): ",
        "deleted_count": "Deleted {} biomes",
        "cancelled": "Operation cancelled",
        "global_overlay_created": "Created global overlay template",
        "no_biomes_to_delete": "No biomes found to delete",
        "creating_backup": "Creating backup...",
        "backup_created": "Backup created: {}",
        "backup_failed": "Backup failed: {}",
        "process_menu": "\nProcessing options:\n1. Process all biomes\n2. Process by group",
        "select_group": "Select group: ",
        "no_groups": "No groups found in {}",
        "group_created": "Group created: {}",
        "group_exists": "Group already exists: {}",
        "enter_group_name": "Enter group name: ",
        "enter_biomes": "Enter biome names (comma separated): ",
        "invalid_group": "Invalid group selection",
        "group_file_created": "Group file created: {}",
        "processing_group": "Processing group: {}",
        "deleting_group": "Deleting group: {}",
        "no_biomes_in_group": "No biomes found in group: {}",
        "invalid_biomes": "Invalid biome names: {}",
        "select_option": "Select option: ",
        "groups_count": "Groups: {}",
    },
    "ru": {
        "welcome": f"Инструмент обработки биомов v{PROGRAM_VERSION}",
        "select_lang": "Выберите язык (en/ru/zh): ",
        "invalid_lang": "Неправильный язык. Текущий язык сохранен.",
        "processing": "Обработка биома: {}",
        "overlay_not_found": "Оверлей не найден: {}",
        "biome_not_found": "Оригинальный биом не найден: {}",
        "success": "Успешно обработано {} биомов!",
        "biomes_missing": "Биомы не найдены в {}",
        "downloading": "Скачивание биомов из Minecraft...",
        "enter_version": "Введите версию Minecraft (например 1.21.8): ",
        "download_success": "Биомы успешно скачаны!",
        "download_failed": "Ошибка загрузки. Скопируйте биомы вручную.",
        "global_overlay_applied": "Глобальный оверлей применен к {} оверлеям",
        "empty_overlays_created": "Создано {} пустых шаблонов оверлеев",
        "menu": "\nГлавное меню:\n1. Обработать биомы\n2. Применить глобальный оверлей\n3. Загрузить биомы из .jar\n4. Создать пустые оверлеи\n5. Сменить язык\n6. Показать информацию\n7. Удалить биомы по группам\n8. Создать группу\n9. Выход\nВыберите опцию: ",
        "invalid_option": "Неправильная опция!",
        "current_lang": "Текущий язык: {}",
        "lang_changed": "Язык изменен на {}",
        "global_overlay_missing": "Глобальный оверлей не найден: {}",
        "no_overlays": "Оверлеи не найдены в {}",
        "no_biomes": "Биомы не найдены в {}",
        "goodbye": "До свидания!",
        "first_run": "Добро пожаловать! Пожалуйста, выберите язык",
        "version_info": "Версия программы: {}\nВерсия биомов: {}",
        "no_biomes_version": "Не загружены",
        "delete_confirm": "Вы уверены, что хотите удалить {} биомов? (y/n): ",
        "deleted_count": "Удалено {} биомов",
        "cancelled": "Операция отменена",
        "global_overlay_created": "Создан шаблон глобального оверлея",
        "no_biomes_to_delete": "Биомы не найдены для удаления",
        "creating_backup": "Создание резервной копии...",
        "backup_created": "Резервная копия создана: {}",
        "backup_failed": "Ошибка создания резервной копии: {}",
        "process_menu": "\nВарианты обработки:\n1. Обработать все биомы\n2. Обработать по группам",
        "select_group": "Выберите группу: ",
        "no_groups": "Группы не найдены в {}",
        "group_created": "Группа создана: {}",
        "group_exists": "Группа уже существует: {}",
        "enter_group_name": "Введите название группы: ",
        "enter_biomes": "Введите названия биомов (через запятую): ",
        "invalid_group": "Неправильный выбор группы",
        "group_file_created": "Файл группы создан: {}",
        "processing_group": "Обработка группы: {}",
        "deleting_group": "Удаление группы: {}",
        "no_biomes_in_group": "Биомы не найдены в группе: {}",
        "invalid_biomes": "Недопустимые названия биомов: {}",
        "select_option": "Выберите опцию: ",
        "groups_count": "Групп: {}",
    },
    "zh": {
        "welcome": f"生物群系处理工具 v{PROGRAM_VERSION}",
        "select_lang": "选择语言 (en/ru/zh): ",
        "invalid_lang": "无效语言。保留当前语言。",
        "processing": "处理生物群系: {}",
        "overlay_not_found": "未找到叠加文件: {}",
        "biome_not_found": "未找到原始生物群系: {}",
        "success": "成功处理 {} 个生物群系!",
        "biomes_missing": "在 {} 中未找到生物群系",
        "downloading": "从Minecraft下载生物群系...",
        "enter_version": "输入Minecraft版本 (例如 1.21.8): ",
        "download_success": "生物群系下载成功!",
        "download_failed": "下载失败。请手动复制。",
        "global_overlay_applied": "全局叠加已应用到 {} 个叠加文件",
        "empty_overlays_created": "已创建 {} 个空叠加模板",
        "menu": "\n主菜单:\n1. 处理生物群系\n2. 应用全局叠加\n3. 从.jar下载生物群系\n4. 创建空叠加文件\n5. 更改语言\n6. 显示信息\n7. 按组删除生物群系\n8. 创建组\n9. 退出\n选择选项: ",
        "invalid_option": "无效选项!",
        "current_lang": "当前语言: {}",
        "lang_changed": "语言已更改为 {}",
        "global_overlay_missing": "未找到全局叠加文件: {}",
        "no_overlays": "在 {} 中未找到叠加文件",
        "no_biomes": "在 {} 中未找到生物群系",
        "goodbye": "再见!",
        "first_run": "欢迎！请选择语言",
        "version_info": "程序版本: {}\n生物群系版本: {}",
        "no_biomes_version": "未下载",
        "delete_confirm": "您确定要删除 {} 个生物群系吗? (y/n): ",
        "deleted_count": "已删除 {} 个生物群系",
        "cancelled": "操作已取消",
        "global_overlay_created": "已创建全局叠加模板",
        "no_biomes_to_delete": "未找到生物群系可删除",
        "creating_backup": "正在创建备份...",
        "backup_created": "备份已创建: {}",
        "backup_failed": "备份失败: {}",
        "process_menu": "\n处理选项:\n1. 处理所有生物群系\n2. 按组处理",
        "select_group": "选择组: ",
        "no_groups": "在 {} 中未找到组",
        "group_created": "组已创建: {}",
        "group_exists": "组已存在: {}",
        "enter_group_name": "输入组名称: ",
        "enter_biomes": "输入生物群系名称 (逗号分隔): ",
        "invalid_group": "无效的组选择",
        "group_file_created": "组文件已创建: {}",
        "processing_group": "正在处理组: {}",
        "deleting_group": "正在删除组: {}",
        "no_biomes_in_group": "在组中未找到生物群系: {}",
        "invalid_biomes": "无效的生物群系名称: {}",
        "select_option": "选择选项: ",
        "groups_count": "组: {}",
    }
}

def load_config():
    """Загружает конфигурацию из файла"""
    default_config = {
        "language": "en",
        "first_run": True,
        "biomes_version": None
    }
    
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                loaded_config = json.load(f)
                return {**default_config, **loaded_config}
        except:
            return default_config
    return default_config

def save_config(config):
    """Сохраняет конфигурацию в файл"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def get_lang(config):
    """Возвращает языковые настройки"""
    return LANGUAGES.get(config.get("language", "en"), LANGUAGES["en"])

def apply_overlay(base_biome, overlay):
    """Применяет оверлей к базовому биому"""
    for i, features in enumerate(overlay.get("features", [])):
        if i < len(base_biome["features"]):
            for feature in features:
                if feature not in base_biome["features"][i]:
                    base_biome["features"][i].append(feature)
        else:
            base_biome["features"].append(features.copy())
    return base_biome

def download_biomes(version, config):
    """Скачивает биомы из Minecraft JAR"""
    lang = get_lang(config)
    print(lang["downloading"])
    minecraft_dir = None
    
    if os.name == 'nt':
        appdata = os.getenv('APPDATA')
        if appdata:
            minecraft_dir = Path(appdata) / '.minecraft'
    else:
        home = Path.home()
        minecraft_dir = home / '.minecraft'
    
    if not minecraft_dir or not minecraft_dir.exists():
        print(lang["download_failed"])
        return False

    jar_path = minecraft_dir / 'versions' / version / f'{version}.jar'
    if not jar_path.exists():
        print(lang["download_failed"])
        return False

    temp_dir = BASE_DIR / "temp_extract"
    temp_dir.mkdir(exist_ok=True)

    try:
        with zipfile.ZipFile(jar_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                if file.startswith('data/minecraft/worldgen/biome/') and file.endswith('.json'):
                    zip_ref.extract(file, temp_dir)
        
        src_dir = temp_dir / 'data' / 'minecraft' / 'worldgen' / 'biome'
        for file in src_dir.glob('*.json'):
            shutil.copy(file, BIOMES_DIR)
        
        config["biomes_version"] = version
        save_config(config)
        
        print(lang["download_success"])
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def process_biomes(config):
    """Основная функция обработки биомов с выбором группы"""
    lang = get_lang(config)
    
    # Проверка наличия биомов
    if not any(BIOMES_DIR.iterdir()):
        print(lang["no_biomes"].format(BIOMES_DIR))
        return
    
    # Проверка наличия оверлеев
    if not any(OVERLAYS_DIR.glob("*.json")):
        print(lang["no_overlays"].format(OVERLAYS_DIR))
        return
    
    # Выбор варианта обработки
    print(lang["process_menu"])
    choice = input(lang["select_option"]).strip()
    
    if choice == "1":  # Обработать все биомы
        biome_files = [f.name for f in OVERLAYS_DIR.glob("*.json") if f.parent != ALL_OVERLAY_DIR]
    elif choice == "2":  # Обработать по группе
        group_files = list(GROUPS_DIR.glob("*.json"))
        if not group_files:
            print(lang["no_groups"].format(GROUPS_DIR))
            return
            
        # Вывод списка групп
        print("\nAvailable groups:")
        for i, group_file in enumerate(group_files, 1):
            print(f"{i}. {group_file.stem}")
        print(f"{len(group_files)+1}. {lang['cancelled']}")
        
        try:
            group_choice = int(input(lang["select_group"]).strip())
            if group_choice == len(group_files)+1:
                print(lang["cancelled"])
                return
            group_file = group_files[group_choice-1]
        except (ValueError, IndexError):
            print(lang["invalid_group"])
            return
        
        # Загрузка группы
        try:
            with open(group_file, 'r', encoding='utf-8') as f:
                group_data = json.load(f)
                biome_files = [f"{b}.json" for b in group_data["biomes"]]
                print(lang["processing_group"].format(group_file.stem))
        except Exception as e:
            print(f"Error loading group: {str(e)}")
            return
    else:
        print(lang["invalid_option"])
        return
    
    # Обработка биомов
    processed_count = 0
    for biome_file in biome_files:
        overlay_path = OVERLAYS_DIR / biome_file
        biome_name = overlay_path.name
        
        if not overlay_path.exists() or overlay_path.parent == ALL_OVERLAY_DIR:
            continue
            
        print(lang["processing"].format(biome_name))
        
        # Загрузка оверлея
        try:
            with open(overlay_path, 'r', encoding='utf-8') as f:
                overlay = json.load(f)
        except FileNotFoundError:
            print(lang["overlay_not_found"].format(biome_name))
            continue
        
        # Загрузка оригинального биома
        original_path = BIOMES_DIR / biome_name
        if not original_path.exists():
            print(lang["biome_not_found"].format(biome_name))
            continue
            
        try:
            with open(original_path, 'r', encoding='utf-8') as f:
                base_biome = json.load(f)
        except Exception as e:
            print(f"Error loading {biome_name}: {str(e)}")
            continue
        
        # Применение оверлея
        modified_biome = apply_overlay(base_biome, overlay)
        
        # Сохранение результата
        output_path = EXPORT_DIR / biome_name
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(modified_biome, f, indent=2, ensure_ascii=False)
        
        processed_count += 1

    print("\n" + lang["success"].format(processed_count))

def apply_global_overlay(config):
    """Применяет глобальный оверлей ко всем оверлеям"""
    lang = get_lang(config)
    
    # Проверка наличия глобального оверлея
    global_path = ALL_OVERLAY_DIR / "all_overlay.json"
    if not global_path.exists():
        print(lang["global_overlay_missing"].format(global_path))
        return
    
    try:
        with open(global_path, 'r', encoding='utf-8') as f:
            global_overlay = json.load(f)
    except Exception as e:
        print(f"Error loading global overlay: {str(e)}")
        return
    
    # Проверка наличия оверлеев
    overlays = list(OVERLAYS_DIR.glob("*.json"))
    if not overlays:
        print(lang["no_overlays"].format(OVERLAYS_DIR))
        return
    
    # Применение глобального оверлея
    processed_count = 0
    for overlay_path in overlays:
        if overlay_path.parent == ALL_OVERLAY_DIR:
            continue
            
        biome_name = overlay_path.name
        print(lang["processing"].format(biome_name))
        
        try:
            with open(overlay_path, 'r', encoding='utf-8') as f:
                overlay = json.load(f)
        except Exception as e:
            print(f"Error loading {biome_name}: {str(e)}")
            continue
        
        # Применяем глобальный оверлей
        for i, features in enumerate(global_overlay.get("features", [])):
            if i < len(overlay.setdefault("features", [])):
                for feature in features:
                    if feature not in overlay["features"][i]:
                        overlay["features"][i].append(feature)
            else:
                while len(overlay["features"]) <= i:
                    overlay["features"].append([])
                overlay["features"][i].extend(features.copy())
        
        # Сохраняем обновленный оверлей
        with open(overlay_path, 'w', encoding='utf-8') as f:
            json.dump(overlay, f, indent=2, ensure_ascii=False)
        
        processed_count += 1

    print("\n" + lang["global_overlay_applied"].format(processed_count))

def create_empty_overlays(config):
    """Создает пустые оверлеи для всех биомов"""
    lang = get_lang(config)
    
    # Проверка наличия биомов
    biomes = list(BIOMES_DIR.glob("*.json"))
    if not biomes:
        print(lang["no_biomes"].format(BIOMES_DIR))
        return
    
    # Создание пустых оверлеев
    created_count = 0
    for biome_path in biomes:
        biome_name = biome_path.name
        overlay_path = OVERLAYS_DIR / biome_name
        
        if not overlay_path.exists():
            empty_overlay = {"features": [[] for _ in range(12)]}
            
            with open(overlay_path, 'w', encoding='utf-8') as f:
                json.dump(empty_overlay, f, indent=2, ensure_ascii=False)
            
            created_count += 1
    
    # Создаем глобальный оверлей, если его нет
    global_path = ALL_OVERLAY_DIR / "all_overlay.json"
    if not global_path.exists():
        empty_overlay = {"features": [[] for _ in range(12)]}
        with open(global_path, 'w', encoding='utf-8') as f:
            json.dump(empty_overlay, f, indent=2, ensure_ascii=False)
        print(lang["global_overlay_created"])
    
    print("\n" + lang["empty_overlays_created"].format(created_count))

def change_language(config):
    """Изменяет язык интерфейса"""
    lang = get_lang(config)
    lang_code = input(lang["select_lang"]).strip().lower()
    if lang_code in LANGUAGES:
        config["language"] = lang_code
        save_config(config)
        lang = get_lang(config)
        print(lang["lang_changed"].format(lang_code))
    else:
        print(lang["invalid_lang"])
    return config

def first_run_setup(config):
    """Обработка первого запуска программы"""
    # Создаем необходимые директории
    for folder in [BIOMES_DIR, OVERLAYS_DIR, ALL_OVERLAY_DIR, 
                   EXPORT_DIR, BACKUPS_DIR, GROUPS_DIR]:
        folder.mkdir(exist_ok=True, parents=True)
    
    # Создаем пример группы при первом запуске
    if config.get("first_run", True):
        lang = get_lang({"language": "en"})
        print(lang["first_run"])
        config = change_language(config)
        
        # Создаем пример группы
        example_group = {
            "name": "example_group",
            "description": "Example biome group",
            "biomes": ["plains", "forest", "mountains"]
        }
        group_path = GROUPS_DIR / "example_group.json"
        if not group_path.exists():
            with open(group_path, 'w', encoding='utf-8') as f:
                json.dump(example_group, f, indent=2, ensure_ascii=False)
            print(lang["group_file_created"].format("example_group.json"))
        
        config["first_run"] = False
        save_config(config)
    
    return config

def show_info(config):
    """Показывает информацию о программе и биомах"""
    lang = get_lang(config)
    biomes_version = config.get("biomes_version", lang["no_biomes_version"])
    print("\n" + lang["version_info"].format(PROGRAM_VERSION, biomes_version))
    
    # Показываем количество групп
    group_count = len(list(GROUPS_DIR.glob("*.json")))
    print(lang["groups_count"].format(group_count))

def delete_biomes_by_group(config):
    """Удаляет биомы по группам"""
    lang = get_lang(config)
    
    # Получаем список групп
    group_files = list(GROUPS_DIR.glob("*.json"))
    if not group_files:
        print(lang["no_groups"].format(GROUPS_DIR))
        return
    
    # Вывод меню удаления
    print("\nAvailable groups:")
    for i, group_file in enumerate(group_files, 1):
        print(f"{i}. {group_file.stem}")
    print(f"{len(group_files)+1}. {lang['cancelled']}")
    
    try:
        group_choice = int(input(lang["select_group"]).strip())
        if group_choice == len(group_files)+1:
            print(lang["cancelled"])
            return
        group_file = group_files[group_choice-1]
    except (ValueError, IndexError):
        print(lang["invalid_group"])
        return
    
    # Загрузка группы
    try:
        with open(group_file, 'r', encoding='utf-8') as f:
            group_data = json.load(f)
            biomes_to_delete = group_data["biomes"]
            print(lang["deleting_group"].format(group_file.stem))
    except Exception as e:
        print(f"Error loading group: {str(e)}")
        return
    
    if not biomes_to_delete:
        print(lang["no_biomes_in_group"].format(group_file.stem))
        return
    
    # Находим файлы, которые реально существуют
    files_to_delete = []
    for biome in biomes_to_delete:
        # Файлы в папке biomes
        biome_file = BIOMES_DIR / f"{biome}.json"
        if biome_file.exists():
            files_to_delete.append(biome_file)
        
        # Файлы в папке overlays
        overlay_file = OVERLAYS_DIR / f"{biome}.json"
        if overlay_file.exists():
            files_to_delete.append(overlay_file)
    
    # Если нечего удалять
    if not files_to_delete:
        print(lang["no_biomes_to_delete"])
        return
    
    # Запрос подтверждения
    confirm = input(lang["delete_confirm"].format(len(files_to_delete))).lower()
    if confirm != 'y':
        print(lang["cancelled"])
        return
    
    # Удаление файлов
    deleted_count = 0
    for file_path in files_to_delete:
        try:
            file_path.unlink()
            deleted_count += 1
        except Exception as e:
            print(f"Error deleting {file_path.name}: {str(e)}")
    
    print("\n" + lang["deleted_count"].format(deleted_count))

def create_group(config):
    """Создает новую группу биомов"""
    lang = get_lang(config)
    
    group_name = input(lang["enter_group_name"]).strip()
    if not group_name:
        print(lang["cancelled"])
        return
    
    # Проверяем, существует ли уже группа
    group_path = GROUPS_DIR / f"{group_name}.json"
    if group_path.exists():
        print(lang["group_exists"].format(group_name))
        return
    
    # Запрашиваем список биомов
    biomes_input = input(lang["enter_biomes"]).strip()
    if not biomes_input:
        print(lang["cancelled"])
        return
    
    # Разбиваем по запятым и убираем пустые значения
    biomes = [b.strip() for b in biomes_input.split(',') if b.strip()]
    
    if not biomes:
        print("Error: Biome list cannot be empty")
        return
    
    # Проверяем валидность названий биомов
    invalid_biomes = []
    for biome in biomes:
        if not (BIOMES_DIR / f"{biome}.json").exists():
            invalid_biomes.append(biome)
    
    if invalid_biomes:
        print(lang["invalid_biomes"].format(", ".join(invalid_biomes)))
        return
    
    # Создаем группу
    group_data = {
        "name": group_name,
        "description": f"Custom biome group: {group_name}",
        "biomes": biomes
    }
    
    with open(group_path, 'w', encoding='utf-8') as f:
        json.dump(group_data, f, indent=2, ensure_ascii=False)
    
    print(lang["group_created"].format(group_name))

def create_backup(config):
    """Создает резервную копию важных папок"""
    lang = get_lang(config)
    
    # Создаем папку для бэкапов, если ее нет
    BACKUPS_DIR.mkdir(exist_ok=True, parents=True)
    
    # Генерируем имя файла с текущей датой и временем
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"backup_{timestamp}.zip"
    backup_path = BACKUPS_DIR / backup_name
    
    print(lang["creating_backup"])
    
    try:
        # Создаем ZIP-архив
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Добавляем папки в архив
            for folder in [EXPORT_DIR, OVERLAYS_DIR, BIOMES_DIR, GROUPS_DIR]:
                if folder.exists():
                    # Рекурсивно обходим все файлы в папке
                    for file in folder.rglob('*'):
                        if file.is_file():
                            # Создаем относительный путь для архива
                            arcname = file.relative_to(BASE_DIR)
                            zipf.write(file, arcname)
        
        print(lang["backup_created"].format(backup_name))
        return True
    except Exception as e:
        print(lang["backup_failed"].format(str(e)))
        return False

def main_menu():
    """Главное меню программы"""
    # Загружаем конфигурацию
    config = load_config()
    
    # Первоначальная настройка
    config = first_run_setup(config)
    
    # Создаем резервную копию при запуске
    create_backup(config)
    
    lang = get_lang(config)
    print(f"\n{lang['welcome']}")
    print(lang["current_lang"].format(config.get("language", "en")))
    
    while True:
        try:
            option = input(lang["menu"]).strip()
            
            if option == "1":  # Обработать биомы
                process_biomes(config)
            elif option == "2":  # Применить глобальный оверлей
                apply_global_overlay(config)
            elif option == "3":  # Загрузить биомы
                version = input(lang["enter_version"])
                if not download_biomes(version, config):
                    print(lang["download_failed"])
            elif option == "4":  # Создать пустые оверлеи
                create_empty_overlays(config)
            elif option == "5":  # Сменить язык
                config = change_language(config)
                lang = get_lang(config)
            elif option == "6":  # Показать информацию
                show_info(config)
            elif option == "7":  # Удалить биомы по группам
                delete_biomes_by_group(config)
            elif option == "8":  # Создать группу
                create_group(config)
            elif option == "9":  # Выход
                print(lang["goodbye"])
                break
            else:
                print(lang["invalid_option"])
        except KeyboardInterrupt:
            print("\n" + lang["goodbye"])
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main_menu()

# ==================================================
# Creator: MrPanda8
# GitHub: https://github.com/MrPanda8/Biome-Tool
# ==================================================