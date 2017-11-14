//Complete this function
static func findPathToNode(rootNode: Node,
                           drawnAtPixel pixel: CGPoint) -> [String]{
    if !((rootNode.frame.origin.x <= pixel.x && pixel.x < rootNode.frame.origin.x + rootNode.frame.size.width) && (rootNode.frame.origin.y <= pixel.y && pixel.y < rootNode.frame.origin.y + rootNode.frame.size.height)) {
        return [String]()
    }
    var path = [String]()
    var potentialChildren: Node?
    var currChildIndex = -1
    for (index, child) in rootNode.children.enumerated() {
        if ((child.frame.origin.x <= pixel.x && pixel.x < child.frame.origin.x + child.frame.size.width) && (child.frame.origin.y <= pixel.y && pixel.y < child.frame.origin.y + child.frame.size.height)) {
            if (currChildIndex < index) {
                potentialChildren = child
                currChildIndex = index
            }
        }
    }
    if let child = potentialChildren {
        return [rootNode.nodeId, child.nodeId]
    }
    return [rootNode.nodeId]
}

static func findPathToNode(rootNode: Node,
drawnAtPixel pixel: CGPoint) -> [String]{
    var path = [String]()
    // No children!
    if (rootNode.children.count == 0) {
      if !((rootNode.frame.origin.x <= pixel.x && pixel.x < rootNode.frame.origin.x + rootNode.frame.size.width) && (rootNode.frame.origin.y <= pixel.y && pixel.y < rootNode.frame.origin.y + rootNode.frame.size.height)) {
        return [String]()
      } else {
        return [rootNode.nodeId]
      }
    } else {
      for child in rootNode.children {
        var tempPath = findPathToNode(child, pixel)
        if (tempPath.count > 0) {
          path += tempPath
        }
      }
    }
    if (path.count == 0) {
      if (rootNode.frame.origin.x <= pixel.x && pixel.x < rootNode.frame.origin.x + rootNode.frame.size.width) && (rootNode.frame.origin.y <= pixel.y && pixel.y < rootNode.frame.origin.y + rootNode.frame.size.height) {
        if (rootNode.nodeId == "root") {
          path = [rootNode.nodeId]
        } else {
          path = ["root", rootNode.nodeId]
        }
      }
    }
    return path
}




static func findPathToNode(rootNode: Node,
drawnAtPixel pixel: CGPoint) -> [String]{
    var path = [rootNode.nodeId]
    // No children!
    if !((rootNode.frame.origin.x <= pixel.x && pixel.x < rootNode.frame.origin.x + rootNode.frame.size.width) && (rootNode.frame.origin.y <= pixel.y && pixel.y < rootNode.frame.origin.y + rootNode.frame.size.height)) {
        return [String]()
      }
    if (rootNode.children.count == 0) {
      if !((rootNode.frame.origin.x <= pixel.x && pixel.x < rootNode.frame.origin.x + rootNode.frame.size.width) && (rootNode.frame.origin.y <= pixel.y && pixel.y < rootNode.frame.origin.y + rootNode.frame.size.height)) {
        return [String]()
      } else {
        return [rootNode.nodeId]
      }
    } else {
      for child in rootNode.children {
        var tempPath = findPathToNode(rootNode: child, drawnAtPixel: pixel)
        if (tempPath.count > 0) {
          path += tempPath
        }
      }
    }
    if (path.count == 0) {
      if (rootNode.frame.origin.x <= pixel.x && pixel.x < rootNode.frame.origin.x + rootNode.frame.size.width) && (rootNode.frame.origin.y <= pixel.y && pixel.y < rootNode.frame.origin.y + rootNode.frame.size.height) {
        if (rootNode.nodeId == "root") {
          path = [rootNode.nodeId]
        }
        else {
          path = ["root", rootNode.nodeId]
        }
      } else{
        path = [String]()
      }
    }
    return path
}
