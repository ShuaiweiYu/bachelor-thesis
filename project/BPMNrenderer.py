from processpiper.text2diagram import render

if __name__ == '__main__':
    input_syntax = """
title: result05
width: 10000
colourtheme: BLUEMOUNTAIN
lane: mail processing unit
	(start) as start
	[collect mail from the party] as activity_13
lane: mail clerk
	[sorts the unopened mail into the various business areas] as activity_14
	[distribute the mail] as activity_15
	[the registry receive the mail] as activity_16
	[open it] as activity_17
	[sort it into groups for distribution] as activity_18
	[register it] as activity_19
lane: assistant registry manager
	[performs a quality check] as activity_20
	<the mail is not compliant?> as gateway_1
	[compile a list of requisition] as activity_3
	[send a list of requisition] as activity_4
	[capture the matter details] as activity_5
	[provide the matter details to the cashier] as activity_6
	<> as gateway_1_end
	<@parallel> as gateway_8
	[puts the receipt and copied documents into an envelope] as activity_9
	[post receipt to the party] as activity_10
	<@parallel> as gateway_8_end
	(end) as end
lane: cashier
	[takes the applicable fees] as activity_7
	[captures the party details] as activity_11
	[print the physical court file] as activity_12

start->activity_13->activity_14->activity_15->activity_16->activity_17->activity_18->activity_19->activity_20->gateway_1
gateway_1-"yes"->activity_3->activity_4->gateway_1_end
gateway_1-"no"->activity_5->activity_6->activity_7->gateway_1_end
gateway_1_end->gateway_8
gateway_8->activity_9->activity_10->gateway_8_end
gateway_8->activity_11->activity_12->gateway_8_end
gateway_8_end->end
       """
    render(input_syntax, "Diagram/output/text05_bpmn.png")
