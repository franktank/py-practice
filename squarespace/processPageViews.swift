
    //Complete this function
    static func processPageViews(pageViews: [PageView]) -> [Int] {
        var pageViewCount = 0
        var visitorCount = 0
        var visitorTracker = [String:Int]()
        var sessionCount = 0
        for pageView in pageViews {
            pageViewCount += 1
            if let previousTimeStamp = visitorTracker[pageView.visitorId] {
                if (pageView.timestamp - previousTimeStamp > 1800) {
                    sessionCount += 1
                }
                visitorTracker[pageView.visitorId] = pageView.timestamp
            } else {
                visitorCount += 1
                sessionCount += 1
                visitorTracker[pageView.visitorId] = pageView.timestamp
            }
        }

        return [pageViewCount, visitorCount, sessionCount]
    }
