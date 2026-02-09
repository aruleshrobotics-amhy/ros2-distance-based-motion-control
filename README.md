
# 🤖 ROS2 Reactive Obstacle Avoidance System

## 📌 Overview

This project implements a modular ROS2-based reactive obstacle avoidance pipeline using Python (`rclpy`).

It demonstrates:

- Sensor data publishing
- Decision-making logic
- Motor command execution
- ROS2 Publisher–Subscriber communication
- Event-driven robotic control

---

## 🏗 System Architecture

DistanceSensor  →  DecisionNode  →  MotorNode  
(Int32)              (String)         (Actuation Log)

Topics:
- `/distance` (std_msgs/Int32)
- `/motion_command` (std_msgs/String`)

---

## 🔹 Node Descriptions

### 1️⃣ Distance Sensor Node (`sensor_node.py`)

- Publishes simulated distance values (1–50)
- Runs on a 1-second timer
- Topic: `/distance`
- Message type: `std_msgs/Int32`

Simulates a basic proximity sensor.

---

### 2️⃣ Decision Node (`decision_node.py`)

- Subscribes to `/distance`
- Applies threshold-based logic
- Publishes motion command

Control Logic:

If distance < 10 → STOP  
Else → MOVE  

Topic published: `/motion_command`  
Message type: `std_msgs/String`

---

### 3️⃣ Motor Node (`motor_node.py`)

- Subscribes to `/motion_command`
- Logs received command
- Simulates actuator behavior

---

## 🧠 Control Strategy

This system implements **reactive control**:

Sensor Input → Immediate Decision → Actuation

Characteristics:
- Deterministic behavior
- No planning
- No memory/state tracking
- Suitable for simple obstacle avoidance systems

---

## ⚙️ How to Run

In separate terminals (after sourcing ROS2):

ros2 run <your_package_name> sensor_node
ros2 run <your_package_name> decision_node
ros2 run <your_package_name> motor_node

Ensure ROS2 environment is properly sourced before execution.

---

## 📚 Concepts Demonstrated

- ROS2 Nodes
- Publisher / Subscriber architecture
- Asynchronous callbacks
- Timers in ROS2
- Topic communication
- Modular robotic system design
- Basic reactive robotics control loop

---

## 🚀 Suggested Improvements

To elevate this project:

- Add ROS2 parameters (configurable threshold)
- Implement hysteresis to prevent oscillation
- Introduce a finite state machine (STOP, MOVE, TURN)
- Integrate PID-based velocity control
- Replace random sensor with structured simulation
- Add launch files
- Add custom message types
- Integrate with Gazebo simulation
- Add unit testing and CI pipeline

---

## 🎯 Learning Outcome

This project builds foundational understanding of:

- ROS2 architecture
- Event-driven robotics systems
- Modular software design for robotics
- Reactive control systems

It serves as a stepping stone toward:

- Autonomous navigation systems
- SLAM integration
- Advanced control systems
- Industrial robotics applications

---

End of README.
