import QtQuick 2.15
import QtLocation 5.15
import QtPositioning 5.15

Rectangle {
    id: root
    width: 1200
    height: 800
    color: "#f0f0f0"
    
    // JavaScript 함수
    function moveToLocation(lat, lng, title) {
        map.center = QtPositioning.coordinate(lat, lng)
        map.zoomLevel = 15
        console.log("이동한 위치: " + title + " (위도: " + lat + ", 경도: " + lng + ")")
    }

    // 상단 컨트롤 패널
    Rectangle {
        id: controlPanel
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        height: 60
        color: "#2c3e50"
        z: 1000
    }

    // 지도 영역
    Map {
        id: map
        anchors.top: controlPanel.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        
        // 울산 중심으로 설정
        center: QtPositioning.coordinate(35.5384, 129.3114)
        zoomLevel: 13
        
        // 지도 제공자 설정 (OpenStreetMap 사용)
        plugin: Plugin {
            name: "osm"
            PluginParameter {
                name: "osm.mapping.providersrepository.disabled"
                value: "true"
            }
        }
        
        // 클릭한 위치 마커
        MapQuickItem {
            id: clickMarker
            visible: false
            anchorPoint.x: 12
            anchorPoint.y: 24
            
            sourceItem: Rectangle {
                width: 24
                height: 24
                color: "red"
                radius: 12
                border.color: "white"
                border.width: 2
                
                Rectangle {
                    anchors.centerIn: parent
                    width: 8
                    height: 8
                    color: "white"
                    radius: 4
                }
            }
        }
        
        // 지도 클릭 이벤트
        MouseArea {
            anchors.fill: parent
            acceptedButtons: Qt.LeftButton
            
            onClicked: function(mouse) {
                var coord = map.toCoordinate(Qt.point(mouse.x, mouse.y))
                
                // 마커 위치 설정 및 표시
                clickMarker.coordinate = coord
                clickMarker.visible = true
                
                // 좌표 정보 팝업 표시
                coordinatePopup.showCoordinate(coord.latitude, coord.longitude, mouse.x, mouse.y)
                
                // 지도 중심을 클릭한 위치로 이동
                moveToLocation(coord.latitude, coord.longitude, "클릭한 위치")
            }
            
            onWheel: function(wheel) {
                if (wheel.angleDelta.y > 0) {
                    map.zoomLevel = Math.min(map.zoomLevel + 0.5, map.maximumZoomLevel)
                } else {
                    map.zoomLevel = Math.max(map.zoomLevel - 0.5, map.minimumZoomLevel)
                }
            }
        }
        


        // 줌 컨트롤
        Column {
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.margins: 20
            spacing: 5
            
            Rectangle {
                width: 40
                height: 40
                color: "white"
                border.color: "#bdc3c7"
                radius: 5
                
                Text {
                    anchors.centerIn: parent
                    text: "+"
                    font.pixelSize: 20
                    font.bold: true
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: map.zoomLevel = Math.min(map.zoomLevel + 1, map.maximumZoomLevel)
                }
            }
            
            Rectangle {
                width: 40
                height: 40
                color: "white"
                border.color: "#bdc3c7"
                radius: 5
                
                Text {
                    anchors.centerIn: parent
                    text: "-"
                    font.pixelSize: 20
                    font.bold: true
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: map.zoomLevel = Math.max(map.zoomLevel - 1, map.minimumZoomLevel)
                }
            }
        }
    }

    // 좌표 정보 팝업
    Rectangle {
        id: coordinatePopup
        width: 200
        height: 60
        color: "white"
        border.color: "#bdc3c7"
        border.width: 1
        radius: 5
        visible: false
        z: 2000
        
        property real targetX: 0
        property real targetY: 0
        
        function showCoordinate(lat, lng, mouseX, mouseY) {
            coordinateText.text = "위도: " + lat.toFixed(6) + "\n경도: " + lng.toFixed(6)
            
            // 팝업 위치 설정 (마우스 클릭 위치 근처)
            targetX = mouseX + 10
            targetY = mouseY - height - 10
            
            // 화면 경계 체크
            if (targetX + width > root.width) {
                targetX = mouseX - width - 10
            }
            if (targetY < 0) {
                targetY = mouseY + 10
            }
            
            x = targetX
            y = targetY
            visible = true
            
            // 3초 후 자동으로 숨김
            hideTimer.restart()
        }
        
        Text {
            id: coordinateText
            anchors.centerIn: parent
            font.pixelSize: 12
            color: "#2c3e50"
            horizontalAlignment: Text.AlignHCenter
        }
        
        // 클릭하면 팝업 숨김
        MouseArea {
            anchors.fill: parent
            onClicked: coordinatePopup.visible = false
        }
        
        Timer {
            id: hideTimer
            interval: 3000
            onTriggered: coordinatePopup.visible = false
        }
    }

}