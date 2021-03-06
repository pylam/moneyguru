/* 
Copyright 2015 Hardcoded Software (http://www.hardcoded.net)

This software is licensed under the "GPLv3" License as described in the "LICENSE" file, 
which should be included with this package. The terms are also available at 
http://www.gnu.org/licenses/gpl-3.0.html
*/

#import <Cocoa/Cocoa.h>
#import "MGOutlinePrint.h"
#import "MGPieChartView.h"

@interface MGSheetPrint : MGOutlinePrint
{
    NSImage *graphImage;
    NSImage *pieImage;
    NSRect graphRect;
    NSRect pieRect;
    NSInteger piePage;
    NSInteger graphPage;
}
- (id)initWithPyParent:(PyGUIObject *)pyParent outlineView:(NSOutlineView *)aOutlineView 
    graphView:(NSView *)aGraphView pieView:(MGPieChartView *)aPieView;
@end