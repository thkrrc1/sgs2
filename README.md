# SGS2使用方法
## 依存パッケージインストール
  ```
  sudo apt install -y \
  python3-pip \
  python3-colcon-clean \
  python3-colcon-common-extensions \
  libqt5svg5-dev \
  qtmultimedia5-dev \
  libqt5multimedia5-plugins \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-ugly \
  gstreamer1.0-libav \
  xserver-xorg-video-dummy \
  ros-jazzy-apriltag \
  open-jtalk \
  open-jtalk-mecab-naist-jdic
  ros-jazzy-srdfdom \
  ros-jazzy-realsense2-camera \
  ```


## slam_toolboxインストール
```terminal
$ cd ~/ros2_ws/src
$ git clone -b jazzy https://github.com/SteveMacenski/slam_toolbox.git
$ cd slam_toolbox
$ git checkout 9b37f20c38890cc340cbabb1777b0d8af6c06f4d
$ cd ~/ros2_ws
$ colcon build --symlink-install
$ source install/setup.bash
```

## 実行方法
### エディタ
```terminal
$ cd ~/sgs2
$ ./sgs_editor_bin
```
### サーバー
```terminal
$ cd ~/sgs2
$ ./sgs_server
```
