
# Ziel: Eine eigene App mit Qt entwickeln

Mithilfe von Qt lassen sich Apps entwickeln, die auf mehreren verschiedenen Betriebssystemen und Geräten laufen können. Bei uns sind das vor allem Laptops mit Linux und die zwei Steamdecks. 

## Zwischenziel 1: Qt Creator installieren

Das Programm mit den wir diese Apps entwickeln heißt Qt Creator. 
Installiere Qt mit dem [Qt Installer](https://www.qt.io/download-qt-installer-oss) und wähle Qt 6.9 for Desktop Development.

Gehe auf Edit -> Preferences  ->  Kits. Und überprüfe, das die Einstellungen so aussehen: 
![[Pasted image 20250524155404.png]]

Wenn das nicht der Fall ist, frag Lennart, Max oder Jurek, wir helfen dir das noch fehlende Zeug zu installieren.

Wenn alles passt, hast du es geschafft!

## Zwischenziel 2:  Ein neues Projekt anlegen

Gehe auf Welcome -> Create Project -> Qt Widgets Application -> Choose

 Gebe einen Projektnamen ein und lege den Speicherort fest. Lege CMake als das Build System fest. Klicke weiter bis das Projekt erstellt ist.

Dein erstes Qt Projekt ist erstellt!

# Qt GUI Projekt: Text und Button mit Reaktion

Dieses Projekt zeigt, wie man mit Qt ein einfaches Hauptfenster erstellt, das ein Textfeld (`QLabel`) und einen Button enthält. Wenn der Button gedrückt wird, wird der Text im Label geändert.

## Projektstruktur

- `mainwindow.h` – Header-Datei der MainWindow-Klasse  
- `mainwindow.cpp` – Aufbau und Logik der Benutzeroberfläche  
- `ui_mainwindow.h` – Automatisch generiert durch Qt Designer (nicht manuell bearbeiten)  

## Ziel

Ein GUI-Fenster, das Folgendes enthält:

- Ein zentriertes Label mit dem Text **„Starttext“**  
- Einen Button mit dem Text **„Five“**  
- Wenn der Button gedrückt wird, ändert sich der Text im Label zu **„Button clicked“**  

## Schritt-für-Schritt-Erklärung

### 1. Konstruktor: Aufbau des Hauptfensters

```cpp
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
```

- Lädt die Benutzeroberfläche (vom Qt Designer), falls verwendet.

### 2. QLabel (Textfeld) erstellen

```cpp
label = new QLabel("Starttext", this);
label->setAlignment(Qt::AlignCenter);
```

- Erstellt ein `QLabel` mit dem Starttext und zentriert es.


### 3. Zentrales Widget & Layout vorbereiten

```cpp
QWidget *centralWidget = new QWidget(this);
this->setCentralWidget(centralWidget);
```

- Legt ein zentrales Widget fest, in dem die anderen Elemente platziert werden.


### 4. Inneres Layout: Label und Button anordnen

```cpp
QVBoxLayout *innerLayout = new QVBoxLayout;
innerLayout->addWidget(label);
```

- Erstellt ein vertikales Layout und fügt das Label ein.


### 5. Button hinzufügen und Signal verbinden

```cpp
QPushButton *button = new QPushButton("Five");
connect(button, &QPushButton::clicked, this, &MainWindow::onButtonClicked);
innerLayout->addWidget(button);
```

- Erstellt einen Button mit dem Text „Five“.  
- Verbindet das `clicked`-Signal mit der Methode `onButtonClicked()`.  

### 6. Äußeres Layout zum Zentrieren verwenden

```cpp
QVBoxLayout *outerLayout = new QVBoxLayout(centralWidget);
outerLayout->addLayout(innerLayout);
outerLayout->setAlignment(innerLayout, Qt::AlignCenter);
```

- Zentriert das gesamte innere Layout in der Mitte des Fensters.


## Destruktor

```cpp
MainWindow::~MainWindow()
{
    delete ui;
}
```

- Gibt den belegten Speicher frei, wenn das Fenster geschlossen wird.

## Button-Funktion

```cpp
void MainWindow::onButtonClicked()
{
    label->setText("Button clicked");
}
```

- Ändert den Text im Label, sobald der Button geklickt wird.

## Erweiterungsmöglichkeiten

- Einen zweiten Button hinzufügen, der den ursprünglichen Text wiederherstellt  
- Einen Zähler integrieren, der mitzählt, wie oft der Button gedrückt wurde  
- Icons oder Farben verwenden, um das Layout optisch aufzuwerten  
- Weitere Steuerelemente wie Textfelder oder Comboboxen hinzufügen  



Der Komplette Code von mainwindow.cpp

 ```cpp
   
#include "mainwindow.h"  
#include "./ui_mainwindow.h"  
#include <QLabel>

MainWindow::MainWindow(QWidget *parent)  
    : QMainWindow(parent)  
    , ui(new Ui::MainWindow)  
{  
    ui->setupUi(this);    label = new QLabel("Starttext", this);  
    QWidget *centralWidget = new QWidget(this);  
    this->setCentralWidget(centralWidget);    
    QVBoxLayout *innerLayout = new QVBoxLayout;
    
    label->setAlignment(Qt::AlignCenter);    QPushButton *button = new QPushButton("Five");  
    
    connect(button, &QPushButton::clicked, this, &MainWindow::onButtonClicked);
    
    innerLayout->addWidget(label);  
    innerLayout->addWidget(button);    
    QVBoxLayout *outerLayout = new QVBoxLayout(centralWidget);  
    outerLayout->addLayout(innerLayout);  
    outerLayout->setAlignment(innerLayout, Qt::AlignCenter); 
    
}

MainWindow::~MainWindow()  
{  
    delete ui;  
}

void MainWindow::onButtonClicked()  
{    label->setText("Button clicked");  
}
```


