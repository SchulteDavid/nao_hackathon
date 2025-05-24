# HTWK‑Robots Hackathon 2025 – **Max‑Stride**‑Lokomotions‑Challenge

Willkommen zur offiziellen Challenge des Reinforcement‑Learning‑Hackathons der HTWK‑Robots! Deine Aufgabe ist es, einen zweibeinigen Simulations­roboter darauf zu trainieren, **mit der größtmöglichen durchschnittlichen Schrittlänge** vorwärts zu laufen – und dabei nicht umzufallen. Alles Notwendige ist bereits auf unserem GPU‑Server installiert: Einfach einloggen, die Reward‑Funktion anpassen und loslegen.

---

## 1 | Reinforcement Learning in 180 Sekunden

Reinforcement Learning (RL) behandelt Regelung als „Versuch & Irrtum“:

| Begriff         | In dieser Challenge                                                                          |
| --------------- | -------------------------------------------------------------------------------------------- |
| **Agent**       | Ein neuronales Netz, das Soll‑Gelenkwinkel für den Roboter ausgibt                           |
| **Umgebung**    | Die Isaac‑Gym‑Physiksimulation (`T1`‑Task) liefert Beobachtungen, Reward und ein `done`‑Flag |
| **Aktion**      | Gewünschte Gelenkwinkel (–1 … 1) pro Steuer­schritt                                          |
| **Beobachtung** | Gravitation, Körper­geschwindigkeiten, Gelenkzustände, Gangphase u. Befehle                  |
| **Reward**      | Skalar, der jeden Zeitschritt misst, wie gut der Agent ist                                   |
| **Ziel**        | Maximierung der *abgezinsten* Reward‑Summe → hier: lange Schritte **und** Überleben          |

Das Netz verbessert sich, indem es viele Simulations­kopien parallel abspielt, Belohnungen sammelt und seine Parameter mit Proximal Policy Optimisation (PPO) aktualisiert. Nach dem Training kann die Policy exportiert und in Echtzeit ausgeführt werden.

---

## 2 | Deine Mission

> **Trainiere eine Policy, die *************************************************************mittlere Schrittlänge************************************************************* über 1 000 Simulations­schritte maximiert und dabei zufällige Stöße übersteht.**

Du darfst **nur** die Reward‑Funktion (Terme & Gewichtungen) verändern – Netzgröße, Algorithmus und Hyperparameter sind fix, damit alle die gleichen Startbedingungen haben. Das Ranking sortiert Einreichungen nach **durch­schnittlicher Schrittlänge (m)**; bei Gleichstand entscheidet **Überlebens­zeit**.

---

## 3 | Schnellstart (💬 „Frag Felix“ ≈ 30 Sekunden)

1. **Web‑Zugang anfordern**  Frag Felix nach den Zugängen für den noVNC‑Client.
2. **Browser öffnen** → du landest auf einem Ubuntu‑Desktop mit vorinstalliertem Isaac Gym, PyTorch 2.2 und VS Code.

Danach kannst du sofort in VS Code loslegen.

---

## 4 | Repo‑Überblick

```
hackathon-maxstride/
├── envs/
│   └── T1.yaml          # Umwelt- & Reward‑Konfiguration
│   └── t1.py            # Task-Implementierung (erbt BaseTask)
├── train.py             # Lernen der Policy
├── play.py              # Ausführen einer trainierten Policy

```

### Wichtige Dateien

| Datei          | Bedeutung                                                              |
| -------------- | ---------------------------------------------------------------------- |
| `tasks/t1.py`  | Definiert Simulation, Beobachtungen **und alle Reward‑Terme**          |
| `envs/T1.yaml` | Enthält die *Gewichte* jedes Reward‑Terms. Wert `0` = Term deaktiviert |
| `train.py`     | Startet das PPO‑Training und speichert Checkpoints & TensorBoard‑Logs  |

---

## 5 | So funktionieren Rewards

In `T1` findest du:

```python
class T1(BaseTask):
    ...
    def _prepare_reward_function(self):
        self.reward_scales = self.cfg["rewards"]["scales"].copy()
        # Terme mit Gewicht 0 werden gestrichen
        for name, scale in self.reward_scales.items():
            self.reward_functions.append(getattr(self, "_reward_" + name))
```

* Jeder Reward‑Term ist eine Methode, die mit `_reward_` beginnt.
* Ist sein Gewicht in `T1.yaml` **ungleich 0**, wird er pro Schritt ausgeführt und mit diesem Gewicht multipliziert.

Einen neuen Reward hinzufügen = **Methode schreiben + Gewicht eintragen**. Mehr Registrierung braucht es nicht.

---

## 6 | Beispiel‑Reward einbauen

1. **Beispiel‑Metric**
   Als Demo fügen wir einen ultrakurzen Reward hinzu, der einfach die *horizontale Vorwärtsgeschwindigkeit* belohnt:

   ```python
   # innerhalb von class T1 ---------------------------------
   def _reward_forward_speed(self):
       return self.base_lin_vel[:, 0]   # positive m/s ⇒ positiver Reward
   # --------------------------------------------------------
   ```

2. **Gewicht in ************************************************************`envs/T1.yaml`************************************************************ setzen**

   ```yaml
   rewards:
     scales:
       forward_speed: 1.0   # aktiviert die Metric
   ```

   Wichtig: Jeder neue Reward **muss** hier unter `rewards: scales:` einen Wert erhalten.
   Ein Wert von `0` blendet den Term aus.

---

## 7 | Training & Ausführen deiner Policy

### Training starten

```bash
python train.py --task=T1
```

* Standardmäßig werden alle Hyperparameter aus `train.py` bzw. `configs/train.yaml` geladen.

* Checkpoints landen unter `logs/<run>/nn/`

### Policy testen

```bash
python play.py --task=T1 --checkpoint=-1   # -1 = letztes Checkpoint
```

Setze `--headless false`, um die Isaac‑Gym‑Vorschau zu sehen.

### Policy exportieren (optional)

```bash
python export_model.py --task=T1 --checkpoint=<iter>
```

Dies erzeugt `model.pt`, falls du die Policy außerhalb des Hackathons verwenden möchtest.
**Für die Challenge ist kein Upload nötig** – die Bewertung erfolgt lokal auf deinem noVNC‑Desktop.

---

## 8 | Troubleshooting & Tipps

* Rewards ausbalancieren – dominiert die Schritt‑Belohnung alles, versucht der Agent evtl. zu springen.

---

Viel Erfolg 🚀 – und möge dein Roboter große Schritte machen!

---

© 2025 HTWK Robots · MIT‑Lizenz
