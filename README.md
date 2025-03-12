# Default Logging Config

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Этот репозиторий содержит примеры настройки логирования в Python. В проекте представлены два основных подхода к настройке логирования:

1. **Простая настройка с использованием `logging.basicConfig`** — это базовый пример, который демонстрирует, как быстро настроить логирование с минимальными усилиями.
2. **Продвинутая настройка с использованием `logging.config.dictConfig`** — этот пример показывает, как можно вынести конфигурацию логирования в отдельный модуль и использовать более гибкий подход для настройки.

---

## Содержание

- [Описание](#описание)
- [Использование](#использование)
  - [Настройка с BasicConfig](#basicconfig)
  - [Настройка с DictConfig](#dictconfig)
- [Лицензия](#лицензия)

---

## Описание

Логгирование — это важная часть любого приложения, позволяющая отслеживать его работу, ошибки и события. В Python стандартная библиотека `logging` предоставляет мощные инструменты для настройки логгирования.

Этот репозиторий демонстрирует два основных способа настройки логгирования:
- **`logging.basicConfig`**: Простой и быстрый способ настройки логгирования для небольших проектов.
- **`logging.config.dictConfig`**: Более гибкий и масштабируемый подход, подходящий для крупных проектов.


## Установка и запуск

Для использования примеров, просто клонируйте репозиторий:

```bash
git clone https://github.com/i-dea-by/default-logging-config.git
cd default-logging-config
python 00_one_file.py
python 01_import_logger.py
```


## Использование


### basicConfig

Файл 00_one_file.py содержит простой пример настройки логирования с использованием logging.basicConfig. 
```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d | %(levelname)-7s | %(module)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)
```

### dictConfig

Файл 01_import_logger.py демонстрирует более сложную настройку логирования с использованием logging.config.dictConfig. Использования различных хэндлеров для разных логов в терминал и файл с использованием фиьтров. 

Конфигурация логирования вынесена в отдельный модуль logger.py.
```python
import logging
from logging.config import dictConfig

from logger import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
log = logging.getLogger(__name__)
```

Пример логов в терминале:
```
[2025-03-12 01:44:26.385] DEBUG    01_import_logger:24 - Start
[2025-03-12 01:44:26.385] DEBUG    01_import_logger:17 - It's DEBUG message
[2025-03-12 01:44:26.386] INFO     01_import_logger:18 - It's INFO message
[2025-03-12 01:44:26.386] WARNING  01_import_logger:19 - It's WARNING message
[2025-03-12 01:44:26.386] DEBUG    01_import_logger:11 - Another DEBUG message
[2025-03-12 01:44:26.386] INFO     01_import_logger:12 - Another INFO message
[2025-03-12 01:44:26.386] WARNING  01_import_logger:13 - Another WARNING message
[2025-03-12 01:44:26.387] DEBUG    01_import_logger:26 - Finish
```

Пример логов в файле `project.log`, создающегося в каталоге /`logs`:
```
[2025-03-12 01:42:33.557] DEBUG    01_import_logger:<module>:23 - Start
[2025-03-12 01:42:33.558] DEBUG    01_import_logger:main:16 - It's DEBUG message
[2025-03-12 01:42:33.558] INFO     01_import_logger:main:17 - It's INFO message
[2025-03-12 01:42:33.558] WARNING  01_import_logger:main:18 - It's WARNING message
[2025-03-12 01:42:33.558] DEBUG    01_import_logger:another_function:10 - Another DEBUG message
[2025-03-12 01:42:33.558] INFO     01_import_logger:another_function:11 - Another INFO message
[2025-03-12 01:42:33.559] WARNING  01_import_logger:another_function:12 - Another WARNING message
[2025-03-12 01:42:33.559] DEBUG    01_import_logger:<module>:25 - Finish
```

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.
