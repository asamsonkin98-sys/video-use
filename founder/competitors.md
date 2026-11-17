# Конкуренты «Обставь» (обставь.рф)

Дата: 17.11.2026. Прогон №2. Сведено из четырёх файлов исследования: `founder/competitors/planners.md` (планировщики и чертежи), `ai.md` (ИИ-дизайн), `retail.md` (маркетплейсы и ритейл), `services.md` (люди и услуги). Описание бизнеса: `founder/idea.md`. Таблица в машинном виде: `founder/competitors.csv`.

## Как собраны данные (прочитать до таблицы)

- **Сайты конкурентов не открывались.** Из облачной сессии WebFetch не резолвил внешние домены (`ENOTFOUND`): remplanner.ru, planoplan.com, planner5d.com, roomtodo.com, ai.neiroset.com, hoff.ru, lemanapro.ru, divan.ru, stolplit.ru, profi.ru, kvadrastudio.ru, proff-remont.ru, korona-remont.ru, а также vc.ru, dtf.ru, sostav.ru, toolfox.ru, hi-tech.mail.ru. avito.ru закрыт для поискового агента.
- **Все факты и цены взяты из поисковой выдачи** (заголовки и фрагменты страниц по указанным ссылкам), а не из прочитанных страниц. Цены у агрегаторов могут отставать от официальных или противоречить друг другу; где источники расходятся, приведены все варианты. Перед `/founder-pricing` цены нужно сверить вручную.
- Многие обзоры на sostav.ru, dtf.ru, vc.ru — блоги и SEO-статьи, часто написанные самими сервисами (подборку [sostav 292124/95684](https://www.sostav.ru/blogs/292124/95684) выдача называет материалом разработчика Remplanner). Их оценки предвзяты.
- «не найдено» / «нет данных» = поиск не показал, а не «у компании этого нет». Доллары в рубли не пересчитывались.
- Авито (Ярославль и РФ) не проверено. Независимых отзывов о российских ИИ-интерьерных сервисах почти нет.

## 1. Таблица конкурентов

Сортировка: от самых прямых к заменителям. Чертежи: М — расстановка мебели, Э — электрика, С — свет, П — полы, Пт — потолки, Р — развёртки, В — ведомости, См — смета.

Для сравнения — **«Обставь»**: план комнаты по размерам, мебель — реальные товары маркетплейсов со ссылками; бесплатно без регистрации; визуализации пакетами 790 ₽ / 10 шт (79 ₽/шт), 1 390 ₽ / 20 (69,50 ₽), 2 390 ₽ / 40 (59,75 ₽), без подписки и без перегенераций; комплект чертежей М, Э, С, П, Пт, Р, В — до 31.12.2026 бесплатно всем (данные основателя, `idea.md`).

### 1.1. Прямые: планировщики с чертежами

| Сервис | Что продаёт | Цена сопоставимого | Чертежи | Реальная мебель магазинов | ИИ | Оплата из РФ | Рейтинг | Главная жалоба |
|---|---|---|---|---|---|---|---|---|
| **Remplanner** ([remplanner.ru](https://remplanner.ru/programma-dlya-dizajna-interera-kvartiry/)) | «рабочих чертежей под капитальный ремонт и визуализации квартиры с подбором материалов в 3D» | Подписка: бесплатный тариф; 690 ₽/мес «Персональный», 1 190 ₽/мес «Расширенный» ([dtf](https://dtf.ru/software/5021300-remplanner-onlajn-planirivshik-remonta)); ранее 1 990 ₽/мес ([toolfox](https://toolfox.ru/services/s/remplanner)); другие обзоры 590–990 ₽/мес и ~20 ₽ за рендер сверх тарифа ([pawetta](https://pawetta.com/servisy/remplanner/), [otzyvmarketing](https://otzyvmarketing.ru/remplanner/)); скидка до 40 % от 3 мес | **Да:** М, Э, П, Пт, Р, См; PDF-комплект и смета только платно ([remplanner.ru](https://remplanner.ru/dizayn_proekt_kvartiry/samostoyatelno/)) | Нет данных; каталог 5 000+ моделей в платном тарифе ([sostav](https://www.sostav.ru/blogs/292124/95327)) | ИИ-рендер из 3D с июля 2026 ([sostav](https://www.sostav.ru/blogs/292124/95327)) | Да | Отзовик 4,0 / 77 отзывов, рекомендуют 74 % ([otzovik](https://otzovik.com/reviews/remplanner_ru-onlayn-planirovschik_kvartir/)) | «Все расчёты в технической документации неверные» ([otzovik](https://otzovik.com/review_15732261.html)) |
| **Planoplan** ([planoplan.com](https://planoplan.com/ru/pricing)) | 2D/3D, рендеры, рабочие чертежи и спецификации | Подписка + токены: «от 1 890 ₽/мес» ([timeweb](https://timeweb.com/ru/community/articles/top-10-neyrosetey-dlya-arhitektury-i-proektirovaniya-platnye-i-besplatnye-ii-generatory-2026-goda)); Лайт 1 890 ₽ ([otzovik](https://otzovik.com/review_18333054.html)); Эксперт 12 500 ₽/3 мес, 40 000 ₽/12 мес ([cad.ru](https://cad.ru/programmnoe_obespechenie/bim_dlya_grazhdanskogo_i_promyshlennogo_stroitelstva/dizayn_i_planirovka/planoplan_1/planoplan/)); 7 дней бесплатно | **Да:** М, Э, Р, В ([блог](https://planoplan.com/es/blog/instructions/floor-plans-layouts-elevations-drawings-and-specs/)) | Не найдено | Не найдено | Да | yareviews 4,7 (24) ([yareviews](https://yareviews.ru/s/planoplan.com)) | Платная версия «себя не оправдывает»: мало мебели, свою не загрузить ([otzovik](https://otzovik.com/reviews/planoplan-programma_dlya_dizayna_interera/)) |
| **Нейросет** ([ai.neiroset.com](https://ai.neiroset.com/ru/furniture-placement)) | План с размерами 2D/3D, ИИ-расстановка «одной кнопкой» по нормам, ИИ-рендер по плану, своя мебель по фото ([unisender](https://www.unisender.com/ru/blog/rasstanovka-mebeli-onlajn/)) | Планировщик бесплатно; токены: пакеты 759–2 799 ₽ ([interior-design](https://ai.neiroset.com/ru/interior-design)), по другим обзорам 379–2 799 ₽, ПРО 2 459 ₽/мес ([unisender](https://www.unisender.com/ru/blog/planirovka-kvartiry-nejrosetyami-onlajn/)) | Экспорт PDF/PNG плана; рабочих чертежей — нет данных | **Не подтверждено**: «каталог с реальными габаритами», о ссылках на маркетплейсы ни слова | **Да** | Да: карты РФ, СБП, SberPay ([vc.ru](https://vc.ru/gdekurs/2734819-luchshie-nevrosseti-dizaina-interera)) | нет данных | На бесплатном тарифе открыта половина каталога ([unisender](https://www.unisender.com/ru/blog/planirovka-kvartiry-nejrosetyami-onlajn/)) |
| **Planner 5D** ([planner5d.com/ru](https://planner5d.com/ru/pricing)) | 2D/3D, HD-рендеры, AR, 8 400+ предметов; AI Designer — автообстановка комнаты ([support](https://support.planner5d.com/en/articles/8540993-ai-designer-furnish-or-style-your-room-with-our-ai-designer-feature-ios)) | App Store РФ: Премиум 1 490 ₽/год, каталог 599 ₽/30 дн. ([App Store](https://apps.apple.com/ru/app/planner-5d-%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%8C%D0%B5%D1%80%D0%B0/id606173978)); сайт 9,99 $/мес или 19,99 $/мес ([everythingxiaomi](https://everythingxiaomi.com/apps/planner-5d/)) | Слабо, без разрезов и ГОСТ ([toolfox](https://toolfox.ru/services/s/planner-5d)); данные противоречат ([sostav](https://www.sostav.ru/blogs/292124/97773)) | Брендовые модели производителей, не российские ([firstchair](https://www.firstchair.app/blog/ai-tools-furnish-empty-room)) | Да | Картой РФ на сайте не подтверждено ([directline](https://www.directline.pro/service/planner5d/)) | Trustpilot 2,5 (~200) по сводке ([directline](https://www.directline.pro/service/planner5d/)) | Списания после триала, отказ в возврате ([directline](https://www.directline.pro/service/planner5d/otzyvy/2/)) |
| **Homestyler** ([homestyler.com](https://www.homestyler.com/pricing?lang=ru_RU)) | 3D, облачный рендер, AI Decoration / Auto-Furnish | Pro 4,90 $ (год) / 9,90 $ (мес), Master 9,90 / 19,90 $ ([fitgap](https://us.fitgap.com/products/008641/homestyler)) | М | Бренды западные/китайские ([inmyroom](https://www.inmyroom.ru/posts/41599-8-onlajn-servisov-kotorye-pomogut-splanirovat-interer-i-ne-pozhalet-ob-ehtom-v-realnosti)) | Да | **Нет**, карты РФ не принимает ([dtf](https://dtf.ru/howto/3923623-oplata-homestyler-v-rossii)) | Trustpilot ~3 ([stork.ai](https://www.stork.ai/en/homestyler)) | Нельзя оплатить из РФ, риск потерять аккаунт ([dtf](https://dtf.ru/howto/3923623-oplata-homestyler-v-rossii)) |
| **Roomtodo** ([roomtodo.com](https://roomtodo.com/en/product/room_planner/)) | Браузерный 2D/3D, рендеры, 360° | Basic 10 $/мес, Pro 20 $/мес; **разово** 4,99 / 9,99 $ за проект ([livejournal](https://spravke.livejournal.com/1284607.html)) | М; бесплатно без PDF ([sostav](https://www.sostav.ru/blogs/292124/95684)) | Не найдено | Не найдено | Не найдено | G2 4,0 (1) ([G2](https://www.g2.com/products/roomtodo/reviews)) | Непонятное управление в 3D ([Trustpilot](https://pl.trustpilot.com/review/roomtodo.com)) |
| **RoomPlan 3D** ([roomplan.ru](https://roomplan.ru/)) | Онлайн-планировщик, 1 400+ моделей, расчёт материалов | 990 ₽/год за всё ([unisender](https://www.unisender.com/ru/blog/programmy-dlya-dizajna-interera-onlajn/)); «от 5 $/мес» ([sostav](https://www.sostav.ru/blogs/292124/95684)) | М, расчёт материалов | Нет, типовой каталог | Не найдено | Да | Не найдено | Только типовые размеры ([vc.ru](https://vc.ru/gdekurs/3037802-planirushchiki-garderobnoy-onlayn)) |
| **«Мой Дом 3D»** (ПК) ([dtf](https://dtf.ru/software/5007087-moy-dom-3d-programma-dlya-proektirovaniya-chastnogo-doma)) | Проект дома/квартиры, инженерные сети, смета | **Разово** от 693 ₽ ([directline](https://www.directline.pro/connect/p/kak-ya-vybirala-programmy-dlya-proektirovaniya-doma/)) | М, Э ([РБК Компании](https://companies.rbc.ru/news/kWMlPahBc1/kak-sdelat-gramotnyij-plan-rozetok-i-vyiklyuchatelej/)), См | Нет | Не найдено | Да | Не найдено | Не найдено |
| **«Дизайн Интерьера 3D»** (AMS, ПК) ([toolfox](https://toolfox.ru/services/s/dizajn-interera-3d)) | 2D → 3D, смета | **Разово** 11 560 ₽ | М, См; без рабочих чертежей | Нет | Не найдено | Да | Не найдено | Не найдено |
| **Intora Plan** ([intora-design.ru](https://intora-design.ru/layout)) | Планировщик по фото плана, PDF ([vc.ru](https://vc.ru/gdekurs/3037802-planirushchiki-garderobnoy-onlayn)) | Базовое бесплатно (ИИ — см. 1.2) | М, PDF | Не найдено | Да | Да | Не найдено | Не найдено |
| **Flat Planner** ([flat-planner.ru](https://flat-planner.ru/)) | Онлайн-планировщик | Бесплатно | М с размерами | Нет, «небольшой каталог типовой мебели» ([unisender](https://www.unisender.com/ru/blog/rasstanovka-mebeli-onlajn/)) | Не найдено | — | Не найдено | Не найдено |
| **«Линейка»** ([lineika.su](https://www.lineika.su/)) | Технический проект: обмер, демонтаж/монтаж, инженерные сети (по выдаче) | Бесплатно | М, сети | Нет | Не найдено | — | Не найдено | Не найдено |
| **Floorplanner** ([floorplanner.com](https://floorplanner.com/pricing)) | 2D/3D, экспорт за кредиты | Plus 5 $/мес, Pro 29 $/мес ([illustrarch](https://illustrarch.com/articles/design-softwares/111930-floorplanner-review.html)) | М | Не найдено | Не найдено | Не найдено | Не найдено | Не найдено |

### 1.2. ИИ-дизайн

| Сервис | Вход | Цена сопоставимого | Реальная мебель | Чертежи | Из РФ | Отзывы / жалобы |
|---|---|---|---|---|---|---|
| **Intora** ([intora-design.ru](https://intora-design.ru/)) | Фото (+ планировщик) | 2 проекта бесплатно; разово 790 ₽ (50 кредитов ≈ 25 генераций), 990 ₽, 2 490 ₽ ([theivansergeev](https://theivansergeev.com/guide-intora/)); в других источниках 490 ₽/мес, «от 379 ₽». Позиционирование: «дизайн интерьера за 60 секунд» ([ichip](https://ichip.ru/podborki/programmy-prilozheniya/nejroset-dlya-dizajna-interera-8-servisov-dlya-foto-komnaty-i-plana-kvartiry-974772)) | нет данных | нет данных | Да: МИР, СБП | «пропорции помещения были немного нарушены» ([theivansergeev](https://theivansergeev.com/guide-intora/)) |
| **room-gpt.ru** ([room-gpt.ru](https://room-gpt.ru/dizajn-komnaty)) | Фото; реальные размеры не учитываются ([unisender](https://www.unisender.com/ru/blog/rasstanovka-mebeli-onlajn/)) | 2 бесплатно; 799 ₽ / 20 генераций; подписка от 1 299 ₽/мес; «Безлимит» 9 999 ₽/30 дн.; 40 → 17 ₽ за генерацию ([sostav](https://www.sostav.ru/blogs/287160/96881)) | нет данных | Нет | Да: МИР, СБП ([sostav](https://www.sostav.ru/blogs/288383/91941)) | нет данных |
| **Kandinsky в ГигаЧате (Сбер)** ([ichip](https://ichip.ru/podborki/programmy-prilozheniya/nejroset-dlya-dizajna-interera-8-servisov-dlya-foto-komnaty-i-plana-kvartiry-974772)) | Фото + правка текстом; «по плану: нет» | Бесплатно, без лимита (по заявлению Сбера) | Нет | Нет | Да, Сбер ID | «стиль подберёт, а влезет ли диван в нишу — не скажет» (ichip) |
| **Домклик (Сбер)**, «примерка» интерьеров ([РИА Недвижимость](https://realty.ria.ru/20250724/domklik-2031211204.html)) | Фото объекта + стиль | Бесплатно ([iXBT](https://www.ixbt.com/news/2025/07/24/bystro-i-besplatno-domklik-sbera-zapustil-primerku-intererov-s-pomoshju-ii.html)) | Нет; результат — референс для заказа дизайн-проекта там же ([Коммерсантъ](https://www.kommersant.ru/doc/7909418)) | Нет | Да | нет данных |
| **Шедеврум / YandexART** ([dtf](https://dtf.ru/dizain_interera/3977654)) | Текст; редизайна по фото не найдено | Бесплатно | Нет | Нет | Да | — |
| **Telegram-боты** (AI Дизайнер, [SYNTX](https://vc.ru/899679-7-luchshih-neirosetei-dlya-dizaina-intererov), [chataibot](https://chataibot.ru/neural/ai-interior-pro/)) | Фото + правки сообщениями ([workspace](https://workspace.ru/blog/dizayn-interera-onlayn-besplatno-5-neyrosetey-kotorye-delayut-dizayn-po-foto-komnaty/)) | нет данных | Нет | Нет | Да | нет данных |
| **Самолёт, чат-бот** ([источник](https://xn--b1agapfwapgcl.xn--p1ai/kak-ispolzovat-nejroset-dlja-sozdanija-proekta-kvartiry/)) | Фото / границы помещения клиента застройщика | Для клиентов застройщика | «каталог реальной мебели» (один вторичный источник) | нет данных | Только экосистема «Самолёта» | — |
| **Room Design AI** ([room-design.ai](https://room-design.ai/nejroseti-dlya-dizaina-interera.php)) | Фото | нет данных | нет данных | Нет | Оплата — нет данных | нет данных |
| **RoomGPT.io** ([roomgpt.io](https://roomgpt.io/fulfillment)) | Фото | $9 / 30 кредитов, $19 / 100, $29 / 200; без подписки ([stork](https://www.stork.ai/en/roomgpt)) | Нет | Нет | В $ | Возврат «на усмотрение руководства» ([политика](https://roomgpt.io/fulfillment)) |
| **Interior AI** ([interiorai.com](https://www.interiorai.com)) | Фото | Pro $49/мес или $29 при оплате за год ([toolsforhumans](https://www.toolsforhumans.ai/ai-tools/interior-ai)) | Нет | Нет | В $ | Trustpilot 2,5 (6) ([Trustpilot](https://ca.trustpilot.com/review/interiorai.com)) |
| **Decor8 AI** ([decor8.ai](https://www.decor8.ai/faqs)) | Фото | $14,99/мес безлимит; API $0,20 за изображение ([toolchase](https://toolchase.com/tool/decor8-ai/)) | Нет | Нет | В $ | 4,2 (toolchase) |
| **Collov AI** ([dataconomy](https://dataconomy.com/2023/12/21/collov-ai-design-features-and-pricing)) | Фото | от $14,99–21/мес ([firstchair](https://www.firstchair.app/blog/collov-alternatives-shoppable-interior-design)) | Частично, зарубежные продавцы | Нет | В $ | [G2](https://www.g2.com/products/collov-ai/reviews), оценка не видна |
| **REimagineHome** ([tooliverse](https://tooliverse.ai/tools/reimagine-home)) | Фото | от $14–19/мес ([tooldirectory](https://tooldirectory.ai/tools/reimaginehome)) | **Да, США:** IKEA, West Elm, Target, Wayfair ([блог](https://www.reimaginehome.ai/blogs/real-product-staging-preview-furniture-shoppable-bundle-1770096134)) | Нет | Каталог бесполезен для РФ | «нет ручного контроля, чтобы поставить конкретный предмет» ([aitoolsbakery](https://aitoolsbakery.com/blog/reimaginehome-review/)) |
| **Decato** ([decato.ai](https://decato.ai/about)) — **референс** | **План** → ИИ обставляет каждую комнату под бюджет, проверяет, что предмет влезает; 3D, рендеры, PDF с ценами | Планирование бесплатно; Pro $20/мес (25 рендеров), Max $100 / $200 ([download](https://decato.ai/download)) | **Да:** IKEA, Wayfair | PDF с ведомостью и ценами | Ритейлеры не российские | Независимых отзывов нет |
| **Zory AI** ([zory.ai](https://zory.ai/en)) | Текст, фото, эскиз или план | нет данных | **Да:** 50+ магазинов, 70 000+ товаров ([topaihubs](https://topaihubs.com/item/zory-ai)) | нет данных | Не российские | нет данных |
| **Wayfair Decorify** ([aboutwayfair](https://www.aboutwayfair.com/category/company-news/wayfair-launches-decorify-a-virtual-room-styler-powered-by-generative-ai)) | Фото | Бесплатно (пилот 2023) | Да, каталог Wayfair ([chainstoreage](https://chainstoreage.com/wayfair-creates-shoppable-home-images-generative-ai)) | Нет | Только США | Окна превращаются в картины ([businessofhome](https://businessofhome.com/articles/wayfair-s-new-tool-shows-ai-s-strengths-and-limitations)) |
| **IKEA Kreativ** ([ikea.com](https://www.ikea.com/au/en/newsroom/range-news/ai-powered-design-experience-ikea-kreativ-launches-pubcf6362b0/)) | Скан комнаты с размерами | Бесплатно ([toolworthy](https://www.toolworthy.ai/tool/ikea-home-design)) | Да, IKEA | Нет | **Нет**, IKEA ушла из РФ | — |

Не подтверждено (SEO-мусор, не опираться): «НейроХолст» с каталогами Леруа Мерлен и Hoff ([fin-pass](https://fin-pass.ru/neyroset-onlayn-dlya-dizayna-interera/); toolfox описывает его как обычный генератор картинок — [toolfox](https://toolfox.ru/services/s/neuroholst)); Flyflat, 1 200 ₽/мес ([golden-tools](https://golden-tools.ru/neyroset-dlya-sozdaniya-vizualizacii-intererov/)), сайт не найден.

### 1.3. Маркетплейсы и ритейл

| Компания | Инструмент | Цена | Вся комната, чужие бренды? | Чертежи | Заметки |
|---|---|---|---|---|---|
| **foorma.ru** ([foorma.ru](https://foorma.ru/), [инструкция](https://foorma.ru/knowledge/marketplace-sync)) — сторонний сервис поверх ритейла | ИИ-примерка реальной мебели по фото комнаты по ссылке на товар WB, Лемана ПРО, Яндекс Маркета | Тарифы **не найдены** | **Да**, мультимаркетплейс | Нет; плана с размерами нет | Самый близкий аналог сценария «мебель с маркетплейса в моей комнате». Похожий бот: [FICHI.AI](https://fichi.ai/bot/primerka-mebeli) |
| **Hoff** ([bg.ru](https://bg.ru/bg/city/city-news/995-ekspress-dizayn)) | AR-приложение ([Google Play](https://play.google.com/store/apps/details?id=com.elarbis.hoff.android&hl=en_GB&gl=US)); платный «экспресс-дизайн»: чертёж расстановки, коллаж, список товаров, от 7 дней | Экспресс-дизайн 15 000 / 20 000 / 25 000 ₽ (студия / 2-комн. / 3-комн.), **цена может быть устаревшей** | Только свой каталог | Чертёж расстановки | Живо ли приложение — неизвестно |
| **Wildberries** ([Газета.Ru](https://www.gazeta.ru/business/news/2024/12/12/24609242.shtml), [WBCON](https://wbcon.ru/2025/03/20/3d-model-wildberries-primerka/)) | AR-просмотр 3D-модели товара | 0 ₽ | Нет, один SKU, модель грузит продавец | Нет | Планировщика комнаты не найдено; пилот для части продавцов ([new-retail](https://new-retail.ru/novosti/retail/wildberries_vnedryaet_vozmozhnost_onlayn_primerki_mebeli_v_realnom_vremeni/)) |
| **Яндекс Маркет** ([comnews](https://www.comnews.ru/content/215503/2021-07-16/2021-w28/yandeksmarket-ukhodit-dopolnennuyu-realnost)) | AR-просмотр 3D-модели | 0 ₽ | Нет, один товар | Нет | Новости 2021 г.; работает ли в 2026 — неизвестно. ИИ-примерка только для одежды ([selsup](https://selsup.ru/blog/ii-primerka-v-yandeks-markete-kak-nejroset-podbiraet-obrazy-i-menyaet-onlajn-shoping-v-rossii/)) |
| **Ozon** ([pixsora](https://pixsora.ru/blog/ar-visualization-product-card-marketplace/), [delovoymir](https://delovoymir.biz/ispolzovanie-arvr-v-kartochkah-tovarov.html)) | 3D в карточках; пилот AR для техники (+21 % конверсии) | 0 ₽ | Нет | Нет | Публичного AR в интерьере нет (гайд 2026) |
| **Лемана ПРО** ([lemanapro.ru/proekt-kuhni](https://lemanapro.ru/proekt-kuhni/)) | 3D-конструктор кухни; бесплатный проект кухни с дизайнером | Бесплатно, без регистрации ([sostav](https://www.sostav.ru/blogs/288383/92154)) | Нет, только свои модули | Спецификация и смета | «не является индивидуальным дизайн-проектом» (там же) |
| **Кухонные салоны** (Мария, Лазурит и др.) ([mnogokuhon](https://www.mnogokuhon.ru/dizajn-proekt-kuhni/), [amic.ru](https://www.amic.ru/news/dizayn-proekt-v-podarok-kak-sdelat-stilnyy-remont-i-ne-razoritsya-518765)) | Замер и бесплатный 3D-проект кухни/шкафа | 0 ₽ (воронка продаж) | Нет, одна зона, своя мебель | Проект кухни, спецификация | — |
| **Столплит** ([пресс-релиз](https://www.stolplit.ru/about/press/news/virtualnaya-primerka-mebeli-ar/), [АиФ](https://aif.ru/society/5067)) | 3D-расстановка онлайн, заказ одной кнопкой; AR в приложении | 0 ₽ | Только своя мебель | М | — |
| **Askona** ([ELARBIS](https://elarbis.com/page46399633.html)) | «Примерить к интерьеру» (WebAR) | 0 ₽ | Нет, один SKU | Нет | Актуальность не подтверждена |
| **Stool Group** ([stoolgroup.ru](https://stoolgroup.ru/tovary-s-dop-realnostyu/)) | AR и скачивание 3D-моделей для дизайнеров | 0 ₽ | Нет | Нет | Возможный источник моделей |
| **Юкея** ([retail.ru](https://www.retail.ru/news/v-rossii-zarabotal-pervyy-ai-marketpleys-mebeli-yukeya-1-iyulya-2026-279459/)) | ИИ-маркетплейс мебели фабрик с 07.2026, без комиссии | — | Подбор от 53 фабрик (данные компании) | Неизвестно | Есть ли план комнаты — неизвестно |
| **Союз-М 3D** ([App Store](https://apps.apple.com/ru/app/%D1%81%D0%BE%D1%8E%D0%B7-%D0%BC-3d-%D0%BC%D0%B5%D0%B1%D0%B5%D0%BB%D1%8C/id1532730115)) | Своя мебель на 3D-сцене, AR | 0 ₽ | Свой каталог | Нет | Нишевое |
| **IKEA** (планировщики) ([ikea.com](https://www.ikea.com/ee/ru/planners/kitchen-planner/)) | Кухня, PAX, Kreativ | 0 ₽ | Только IKEA | Список товаров | Купить в РФ нельзя |

Мегамаркет, Divan.ru, OBI, Петрович (как планировщик), Шатура, Много Мебели, Стильные кухни, Swed House: инструментов в выдаче не найдено.

### 1.4. Люди и услуги

| Кто | Цена | Что входит | Сроки | Источник |
|---|---|---|---|---|
| Профи.ру, дизайн интерьера, Ярославль | 950–3 200 ₽/м² (другие версии страницы: 500–1 750; 500–2 000, «в среднем 1 000»); планировочное решение 8 000–10 000 ₽; рабочая документация у исполнителя 600 ₽/м² | разное | — | [profi.ru](https://profi.ru/geo-yar/remont/design/dizain-interiera/price/), [дизайн-проект](https://profi.ru/geo-yar/remont/design/dizain-interiera/dizain-proekt/) |
| Яндекс Услуги, Ярославль (117 исполнителей, ср. рейтинг 4,6) | 600–2 200 ₽/м²; несколько исполнителей (в т. ч. «ПРОДИЗАЙН») от 2 000 ₽/м²; планировочное решение 450, полный проект с 3D 1 800 ₽/м² | у «от 2 000»: рабочие чертежи, 3D, смета | — | [uslugi.yandex.ru](https://uslugi.yandex.ru/16-yaroslavl/category/dizajneryi/dizajner-intererov/dizajn-proekt-interera-kvartiryi--261) |
| «Профф-Ремонт» Ярославль | дизайн-проект **от 465 ₽/м²**; 5 рендеров 450 ₽/м² | пример: 32 листа, 13 планов, 7 развёрток, 21 визуализация | от 3 недель на комнату | [proff-remont](https://yaroslavl.proff-remont.ru/dizajn_interyera/kvartira/), [цены](https://yaroslavl.proff-remont.ru/ceny/) |
| «Корона» Ярославль | квартира от 699, комната от 500 ₽/м²; технический проект от 550 ₽/м² | М, выключатели, розетки, освещение, электроразводка, ведомость отделки | — | [korona-remont](https://yaroslavl.korona-remont.ru/dizayn-interiera/kvartiry) |
| Студия «Квадра», Ярославль | от 2 500 / 3 500 / 5 000 ₽/м² (главная); на других страницах 900 / 1 300 / 1 900 и «от 1 500» | концепция → + чертежи → + надзор | — | [kvadrastudio.ru](https://kvadrastudio.ru/), [/dizajn-interera](https://kvadrastudio.ru/dizajn-interera) |
| InteriorDesignStudio (InMyRoom), Ярославль | технический проект 2 000, полный с визуализациями 3 500 ₽/м² | планировка, освещение, розетки, сантехника, полы | — | [inmyroom](https://www.inmyroom.ru/yaroslavl/services/profession/dizajner-interera) |
| Make Art, Ярославль | от 1 200 ₽/м² | — | — | [makeart-ds.ru](https://makeart-ds.ru/) |
| Ремонтные компании, «дизайн-проект в подарок» | 0 ₽ при ремонте под ключ (дизайнерский ремонт от 11 900–15 000 ₽/м²) | обмер, 3D, электрика, ведомость | — | [proff-remont](https://yaroslavl.proff-remont.ru/dizajnerskij_remont/), [korona-remont](https://yaroslavl.korona-remont.ru/) |
| YouDo | планировочное решение 5 500 ₽; 3D-планировка с мебелью от 3 400 ₽; дизайн-проект 1-комн. 10 200 ₽ | — | — | [youdo](https://remont.youdo.com/interior/dizproekt/flats/price), [3D с мебелью](https://youdo.com/bytovoj-remont/interior/3d/quarters/diz/mebel) |
| ReRooms (онлайн) | комната 14 990 ₽ фикс. (на других страницах 19 990) | планировка, коллажи, 3D, ведомости; чертежи на ряде страниц не входят | квартира 20–45 дн. | [rerooms.ru](https://rerooms.ru/) |
| Ars Omnis (онлайн) | 12 000 / 24 000 / 30 000 ₽ за комнату | пакеты | от 10 раб. дн. | [arsomnis.ru](http://arsomnis.ru/fix_cena.html) |
| designershelp.ru (онлайн) | 28 000 ₽ за комнату | — | 10 раб. дн. | [designershelp.ru](https://designershelp.ru/dizajn-interera-komnaty-onlajn/) |
| «Мой дом» (онлайн) | от 15 000 ₽ (без чертежей); технический от 30 000 ₽ | — | от 5–10 дн. | [my-dom.design](https://my-dom.design/stoimost-dizajna-kvartiry/) |
| Профи.ру, Москва | 920–3 050 ₽/м²; дизайн-проекты 1 000–4 000 | — | — | [profi.ru](https://profi.ru/remont/design/dizain-interiera/price/) |
| Проект электрики отдельно | 8 500–20 000 ₽ за квартиру (≈120–200 ₽/м²); у электромонтажников часто бесплатно под монтаж | схема розеток, выключателей, групп | — | [mskgrp](https://mskgrp.ru/price/price-list-na-proekt-elektriki), [energy-systems](https://energy-systems.ru/elektrosnabzhenie-kvartiry), [arhibald](https://arhibald.ru/articles/proekt-elektriki-kvartiry), [realty.yandex](https://realty.yandex.ru/journal/post/shema-elektroprovodki-v-kvartire/) |

### 1.5. Заменители (решить самому, без сервиса)

| Что | Цена | Источник |
|---|---|---|
| **Sweet Home 3D** — бесплатная открытая программа, печать плана в PDF | 0 ₽ | [sweethome3d.com](https://www.sweethome3d.com/ru/index.jsp) |
| **SketchUp** — универсальное 3D, чертежи вручную | Go 129 $/год, Pro 399 $/год (сторонние данные) | [myarchitectai](https://www.myarchitectai.com/blog/sketchup-pricing) |
| **Конструкторы шкафов**: M-Click, Blum | 0 ₽ | [dtf](https://dtf.ru/id3454342/5012935-besplatnyy-3d-konstruktormebeli-m-click), [blum.com](https://www.blum.com/md/ru/services/planning-construction-product-selection/cabinet-configurator/) |
| **Готовые типовые проекты PDF**: «Петрович» от 46 990 ₽, Студия Марии Михайловой 49 900 ₽, Дизайн.Маркет (цена не найдена) | 41 990–49 900 ₽ | [petrovich](https://moscow.petrovich.ru/services/design/), [mikhailova-design](https://mikhailova-design.ru/gotovye-dizajn-proekty-kvartir-i-domov-s-chertezhami), [design-market](https://design-market.ru/) |
| **Курсы «проект своей квартиры»**: Нетология 64 200 ₽, Pentaschool 71 645 ₽, Grafium 990–10 990 ₽, бесплатные Skillbox и Нетология (SketchUp) | 0–71 645 ₽ | [ledigital](https://ledigital.ru/course/dizayn-proekt-kvartiry-kurs-dlya-sebya), [pentaschool](https://pentaschool.ru/program/dizajn-zhilogo-interera-s-nulya), [grafium](https://grafium.pro/designproject-sk), [skillbox](https://intensive.skillbox.ru/interior-designer/), [netology](https://netology.ru/programs/dizajner-intererov-demo) |
| **AR-примерка одного товара в приложении маркетплейса** (WB, Яндекс Маркет) + рулетка | 0 ₽ | см. 1.3 |

## 2. Диапазон цен на сопоставимое

Минимум, медиана и максимум — по ценам из таблиц выше; медиана посчитана мной по перечисленным точкам, а не взята из источника.

| Что сравниваем | Минимум | Медиана (по точкам) | Максимум | «Обставь» |
|---|---|---|---|---|
| **Одна ИИ-визуализация / рендер** (рубли) | 0 ₽ (Kandinsky, Домклик) | ≈ 20–32 ₽: Remplanner ~20 ₽ сверх тарифа, Intora 790 ₽ / ≈25 генераций ≈ 32 ₽ (мой расчёт) | 40 ₽ (room-gpt.ru, 799 ₽ / 20); рынок в целом 17–40 ₽ | 59,75–79 ₽ — **выше рынка** |
| **DIY-планировщик с чертежами** | 0 ₽ (Sweet Home 3D, «Линейка», бесплатный Remplanner без PDF) | 690–1 190 ₽/мес (Remplanner) | Planoplan от 1 890 ₽/мес; Эксперт 40 000 ₽/год | комплект чертежей 0 ₽ до 31.12.2026 |
| — разовая оплата | «Мой Дом 3D» от 693 ₽ | Roomtodo 4,99–9,99 $ за проект | «Дизайн Интерьера 3D» 11 560 ₽ | пакеты 790–2 390 ₽ |
| **Проект комнаты 15 м² у людей** | 0 ₽ (в подарок при ремонте); планировка 3 400–5 500 ₽ (YouDo) | ≈ 15 000 ₽ (ReRooms 14 990, Hoff 15 000) | 75 000 ₽ с надзором (5 000 ₽/м², «Квадра») | — |
| — полный проект у ярославского дизайнера | от 465 ₽/м² ≈ 7 000 ₽ («Профф-Ремонт») | 1 500–2 500 ₽/м² ≈ 22 500–37 500 ₽ | 3 500–5 000 ₽/м² | — |

## 3. Карта позиционирования (текстом)

Две оси, которые важны покупателю «влезет ли и что купить»:
- **По горизонтали — насколько результат годится для реальной комнаты:** картинка по фото (размеры «на глаз») → план с размерами → рабочие чертежи для ремонта.
- **По вертикали — можно ли купить то, что на картинке:** выдуманная или типовая мебель → один товар / один магазин → много магазинов со ссылками.

```
                     МОЖНО КУПИТЬ: МНОГО МАГАЗИНОВ
                               |
   foorma.ru (фото+WB/ЯМ/Лемана)|   Decato, Zory (план + магазины, но не РФ)
   REimagineHome, Decorify (US)|
                               |                          ★ ОБСТАВЬ
                               |                 (план + WB/Ozon/ЯМ + чертежи)
-------------------------------+-------------------------------------------
   AR WB / Яндекс Маркет, Askona|   Столплит 3D, IKEA, Лемана ПРО (кухня)
   (1 SKU в камере)            |   Hoff экспресс-дизайн 15–25 тыс. ₽
   Домклик (→ проект у Сбера)   |   Кухонные салоны (бесплатно, своя мебель)
                     ОДИН МАГАЗИН / ОДИН ТОВАР
-------------------------------+-------------------------------------------
   Intora, room-gpt.ru,        |   Нейросет (план + ИИ, мебель ? )
   Kandinsky, боты, Interior AI|   Planner 5D, Homestyler (из РФ не оплатить)
   (17–40 ₽ / 0 ₽ за картинку)  |   Remplanner, Planoplan (чертежи, подписка)
                               |   Дизайнеры 465–5 000 ₽/м², «Мой Дом 3D»
                     ТИПОВАЯ ИЛИ ВЫДУМАННАЯ МЕБЕЛЬ
 ФОТО, РАЗМЕРЫ НА ГЛАЗ  <------------------------------>  ПЛАН + ЧЕРТЕЖИ
```

Третья ось — цена и модель оплаты: почти все планировщики берут **подписку** (Remplanner, Planoplan, Planner 5D, Homestyler, Floorplanner, SketchUp); разово — Roomtodo, ПК-программы, Intora, RoomGPT.io и «Обставь». Люди стоят на порядок дороже, но дают замер и ответственность.

## 4. Жалобы в категории (от частых к редким)

Число — сколько независимых источников с этой жалобой нашлось; «тонко» — меньше трёх.

1. **Мебель, которую нельзя купить, и бедный каталог (5 источников).** «ИИ способен придумать правдоподобный комод или светильник, который невозможно купить в точности» ([habr/bothub](https://habr.com/ru/companies/bothub/articles/1083726/)); «мебель на её картинках часто не существует в продаже, а размеры не сходятся с реальными» ([nostress-design](https://nostress-design.ru/journal/neyroseti-v-dizayne-interyera/)); Planoplan: мало мебели, свою не загрузить ([otzovik](https://otzovik.com/reviews/planoplan-programma_dlya_dizayna_interera/)); Flat Planner — «небольшой каталог типовой мебели» ([unisender](https://www.unisender.com/ru/blog/rasstanovka-mebeli-onlajn/)); RoomPlan 3D — только типовые размеры ([vc.ru](https://vc.ru/gdekurs/3037802-planirushchiki-garderobnoy-onlayn)).
2. **Неточные размеры и пропорции (6 источников).** Remplanner: «Все расчёты в технической документации неверные», не учитывается толщина стен ([otzovik](https://otzovik.com/review_15732261.html)); стена фиксирована 10 см, глючит ([irecommend](https://irecommend.ru/content/pomozhet-rasstavit-mebel-vybrat-tona-i-sorientirovatsya-v-prostranstve-ostalnoe-tolko-profes)); ИИ: «диван — непропорционально широким» ([vc.ru](https://vc.ru/services/3189894-dizayn-interera-s-pomoshchyu-neyroseti)); «сохрани размеры» не гарантирует метрическую точность ([skillmagnet](https://skillmagnet.ru/guides/articles/nejroset-dlya-dizajna-interera.html)); Intora — «пропорции помещения были немного нарушены» ([theivansergeev](https://theivansergeev.com/guide-intora/)); Decorify превращает окна в картины ([businessofhome](https://businessofhome.com/articles/wayfair-s-new-tool-shows-ai-s-strengths-and-limitations)).
3. **Подписки и автосписания (4 источника).** Planner 5D: списания после пробного периода и отказ в возврате ([directline](https://www.directline.pro/service/planner5d/otzyvy/2/), [directline](https://www.directline.pro/service/planner5d/otzyvy/4/)); русские «нейросети»-агрегаторы: триал за 1 ₽, потом около 2 000 ₽ ([otzovik](https://otzovik.com/reviews/onlayn-neyroset_rf-chatgpt_4_bez_vpn_i_na_russkom_yazike/), [otzovik](https://otzovik.com/reviews/usegpt_ru-neyroset_chatgpt_5/)).
4. **Платная стена и «дорого для не-дизайнера» (4 источника).** Remplanner — платная версия «дорогая и неточная» ([otzovik](https://otzovik.com/reviews/remplanner_ru-onlayn-planirovschik_kvartir/)); Planoplan — цена «великовата» ([otzovik](https://otzovik.com/reviews/planoplan-programma_dlya_dizayna_interera/)); Нейросет — на бесплатном тарифе половина каталога ([unisender](https://www.unisender.com/ru/blog/planirovka-kvartiry-nejrosetyami-onlajn/)); Planner 5D — урезанная бесплатная версия ([kimola](https://kimola.com/reports/explore-key-insights-from-planner-5d-user-reviews-google-play-tr-148447)).
5. **Нельзя оплатить из России (2 источника, тонко).** Homestyler — карты РФ не принимаются, риск потерять аккаунт ([dtf](https://dtf.ru/howto/3923623-oplata-homestyler-v-rossii)); Planner 5D — оплата картой РФ на сайте не подтверждена ([directline](https://www.directline.pro/service/planner5d/)).
6. **Сложно и медленно (2 источника, тонко).** Roomtodo — непонятное управление в 3D ([Trustpilot](https://pl.trustpilot.com/review/roomtodo.com)); Planoplan — медленная онлайн-версия ([junior3d](https://junior3d.ru/article/planoplan.html)).
7. **Мало контроля над ИИ (1 источник, тонко).** REimagineHome: нельзя поставить конкретный предмет вручную ([aitoolsbakery](https://aitoolsbakery.com/blog/reimaginehome-review/)).

У людей-дизайнеров публичных жалоб в исследовании не собирали; их минусы по фактам — сроки от 5–10 дней до 3–6 недель и цена ([services.md](competitors/services.md)).

## 5. Пробел, который может занять «Обставь»

**В России никто не найден, кто делает всё сразу: план комнаты с реальными размерами + реальная мебель из разных маркетплейсов (WB, Ozon, Яндекс Маркет) со ссылками на покупку + комплект рабочих чертежей для ремонта + разовая оплата в рублях.**

Доказательства по звеньям:
- План с размерами есть у многих (Нейросет, Remplanner, Planner 5D, Homestyler, Intora).
- Реальная мебель со ссылками: в РФ — только AR одного SKU у WB, бот «Самолёта» (закрытая экосистема) и foorma.ru (по фото, без плана). Интеграции планировщика с WB/Ozon поиск не нашёл ([unisender](https://www.unisender.com/ru/blog/rasstanovka-mebeli-onlajn/)).
- Рабочие чертежи для DIY — Remplanner и Planoplan, но по подписке и без покупаемой мебели.
- Ритейлеры решают «один товар» или «одна зона своей мебелью» ([vc.ru: AR почти всегда привязан к конкретному SKU](https://vc.ru/retail/2901923-ai-primerka-v-mebelnom-e-commerce-zamena-ar-xr)).
- Главная жалоба категории — «мебель нельзя купить, размеры не сходятся» (раздел 4, п. 1–2) — это ровно то, что закрывает «Обставь».
- За рубежом связка уже есть (**Decato**: план → ИИ обставляет товарами IKEA/Wayfair с проверкой «влезает» → PDF с ценами), значит, модель востребована, но ров не технологический.

Оговорка: у Нейросета наличие ссылок на маркетплейсы **не подтверждено и не опровергнуто**, а у foorma.ru неизвестны тарифы и точность. Если ручная проверка покажет, что у кого-то из них это уже есть, пробел сужается до «чертежи + мультимагазин + разовая оплата».

## 6. Три главные угрозы

1. **Нейросет добавит ссылки на маркетплейсы.** У него уже есть план с размерами, ИИ-расстановка «одной кнопкой» по нормам, ИИ-рендер, своя мебель по фото, рубли и СБП ([unisender](https://www.unisender.com/ru/blog/rasstanovka-mebeli-onlajn/), [vc.ru](https://vc.ru/gdekurs/2734819-luchshie-nevrosseti-dizaina-interera)). Не хватает только реальных товаров со ссылками — достаточно подключить фид WB/Ozon. Срок — недели-месяцы. Это и есть задуманный «Обставь» ИИ-дизайн.
2. **Remplanner.** Ближайший конкурент по чертежам: рубли, бесплатный тариф, электрика, отделка, развёртки, смета, ИИ-рендер с июля 2026 ([sostav](https://www.sostav.ru/blogs/292124/95327)), 77 отзывов на Отзовике. Ему нужно добавить каталог маркетплейсов или снизить платную стену, чтобы закрыть преимущество «Обставь» по чертежам.
3. **Маркетплейсы и экосистема Сбера.** У WB и Яндекс Маркета есть 3D-модели с реальными габаритами и бесплатная загрузка моделей продавцами ([АВОШОП](https://avoshop.ru/company/news/2024/wildberries_testiruem_zagruzku_3d_modeley_mebeli_v_kartochki_tovarov/), [rozetked](https://rozetked.me/news/19818-yandeks-market-poluchil-funkciyu-ar-prosmotra-krupnoy-bytovoy-tehniki-i-elektroniki)); Ozon видел +21 % конверсии от AR ([delovoymir](https://delovoymir.biz/ispolzovanie-arvr-v-kartochkah-tovarov.html)). У Сбера уже есть бесплатный Kandinsky, Домклик с «примеркой» интерьеров и дизайн-проектом в том же разделе ([Коммерсантъ](https://www.kommersant.ru/doc/7909418)): если Домклик добавит план с размерами и товары Мегамаркета, он получит всю цепочку и трафик. Оценка из `retail.md`: средняя вероятность за 1–2 года, высокий ущерб. Ограничение: маркетплейс покажет только свои товары, а чертежи для строителей ему не нужны. Промежуточная угроза — **foorma.ru**, который уже берёт товары WB, Лемана ПРО и Яндекс Маркета по ссылке.

## 7. Что это значит для «Обставь»

### Цены
- **Визуализации дороже рынка.** 59,75–79 ₽ за изображение против 17–40 ₽ у room-gpt.ru и ~20 ₽ у Remplanner, а Kandinsky и Домклик — бесплатно. Продавать рендер как «красивую картинку» нельзя: покупатель найдёт дешевле. Продавать как «картинку по точному плану с мебелью, которую можно купить по ссылке». Отсутствие перегенераций при цене выше рынка — риск жалоб по п. 2 раздела 4 (ИИ-пропорции); это стоит учесть в оффере.
- **Чертежи с января 2027.** Опора — Remplanner 690–1 190 ₽/мес, где PDF-комплект и смета только платно. Разовый пакет чертежей в районе одного–двух месяцев Remplanner бьёт в его платную стену и в жалобу «подписки и автосписания». Верхняя опора — самые дешёвые люди: планировка 3 400–5 500 ₽ (YouDo), проект от 465 ₽/м² ≈ 7 000 ₽ за 15 м² («Профф-Ремонт»), экспресс-дизайн Hoff 15 000 ₽. Разовые аналоги: «Мой Дом 3D» от 693 ₽, Roomtodo 4,99–9,99 $ за проект.
- **Сравнение с дизайнером переформулировать.** Тезис «в Ярославле от 2 000 ₽/м²» как нижняя граница неверен: на рынке есть 465 ₽/м² («Профф-Ремонт»), 500–699 ₽/м² («Корона»), 380–950 ₽/м² снизу у Профи.ру и «проект в подарок» при ремонте. Честно: «В Ярославле дизайн-проект стоит от 500 до 3 000+ ₽/м²; полный проект с чертежами у дизайнера — около 1 500–2 500 ₽/м², то есть 20 000–40 000 ₽ за комнату 15 м²» ([services.md](competitors/services.md)). Состав чертежей «Обставь» совпадает с рабочим проектом дизайнера (у «Короны» и «Профф-Ремонта» — те же планы электрики, света, полов, потолков, развёртки), но без замера, надзора и ответственности — об этом надо говорить прямо.
- **Разовая оплата — сохранить.** Почти все планировщики продают подписку; громкие жалобы рынка — автосписания (Planner 5D, агрегаторы нейросетей). «Без подписки» — аргумент в рекламе.

### Позиционирование
- Главный посыл — «примерь реальную мебель с WB, Ozon и Яндекс Маркета в комнате с точными размерами до покупки — и получи чертежи для ремонта». Это закрывает две главные жалобы категории (мебель не купить; размеры не сходятся).
- Не обещать «дизайн-проект кухни»: это поле бесплатно заняли Лемана ПРО, Hoff и кухонные салоны.
- Против маркетплейсов — мультимагазинность: диван с WB и шкаф из Лемана ПРО в одной комнате; маркетплейс покажет только свои товары. Партнёрские ссылки делают «Обставь» источником трафика для маркетплейса, а не конкурентом.
- Против дизайнеров — скорость (сразу против 5 дней — 6 недель) и цена; честно говорить, чего нет (замер, надзор).
- Против SketchUp и курсов — «замена SketchUp для непрофессионала»: люди платят за курсы (до 71 645 ₽) и готовые PDF-проекты (41 990–49 900 ₽), чтобы делать самим.

### ИИ-ров
- **ИИ-расстановка сама по себе не уникальна:** она уже есть у Нейросета (в рублях), Homestyler, Planner 5D, а за рубежом Decato делает ровно «план → ИИ обставляет → PDF с ценами». Технологией ров не удержать.
- **Что действительно уникально в РФ по найденным данным:** реальные товары WB/Ozon/Яндекс Маркета **с нормализованными габаритами** (у WB габариты часто указаны только текстом — [new-retail](https://new-retail.ru/novosti/retail/wildberries_vnedryaet_vozmozhnost_onlajn_primerki_mebeli_v_realnom_vremeni/)) в плане с размерами + комплект рабочих чертежей + разовая оплата. Ров — это собственная проверенная база габаритов, качество фидов, «Своя мебель» по ссылке/скриншоту и связка с чертежами, которые маркетплейсу и ИИ-рендерам не нужны.
- Скорость важнее секретности: окно до того, как Нейросет подключит фид маркетплейса, по оценке `ai.md` — недели-месяцы.

## 8. Проверить руками

- **Нейросет** ([ai.neiroset.com](https://ai.neiroset.com/ru/furniture-placement)): есть ли ссылки на товары WB/Ozon/Я.Маркета в каталоге; актуальные цены токенов и подписок (источники дают 379–2 799 ₽ и ПРО 2 459 ₽/мес); есть ли рабочие чертежи.
- **foorma.ru** ([foorma.ru](https://foorma.ru/)): тарифы; точность размеров при примерке по фото; можно ли задать план комнаты.
- **Remplanner** ([remplanner.ru](https://remplanner.ru/programma-dlya-dizajna-interera-kvartiry/)): актуальные тарифы (690 / 1 190 / 1 990 ₽/мес или 590–990), что входит в бесплатный тариф, цена рендера, работает ли ИИ-рендер, есть ли интеграция с магазинами.
- **Decato** ([decato.ai](https://decato.ai/about)) как референс: пройти путь «план → ИИ обставляет → проверка “влезает” → PDF с ценами», посмотреть упаковку тарифов ($20/мес за 25 рендеров).
- Попутно: Авито-услуги Ярославля; актуальность экспресс-дизайна Hoff 15–25 тыс. ₽; работает ли AR у WB и Яндекс Маркета в 5–10 карточках диванов. Для повторной проверки из сессии нужно разрешить в сети домены сервисов и СМИ.

Следующий шаг: `/founder-consumer` использует жалобы раздела 4 как реальные возражения; `/founder-pricing` — диапазоны раздела 2.
