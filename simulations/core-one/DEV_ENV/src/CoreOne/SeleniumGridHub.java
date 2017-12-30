/*     
 *  Module Author         : Neal DeBuhr
 *  Module Date           : 27-December-2017  
 *  DEVS Suite Author     : Savitha and Anindita ACIMS(Arizona Centre for Integrative Modeling & Simulation)
 *  DEVS Version          : DEVSJAVA 2.7 
 *  DEVS Date             : 15-April-2012
 *
 *  This component model handles the distribution of test cases to test executor nodes
 */
package CoreOne;

import GenCol.*;
import model.modeling.*;
import model.simulation.*;
import view.modeling.ViewableAtomic;
import view.simView.*;

public class SeleniumGridHub extends ViewableAtomic {// ViewableAtomic is used instead
    // of atomic due to its
    // graphics capability
    protected Queue jobs_queue;
    protected int number_nodes;
    protected int number_jobs;
    protected int node_ready;
    protected int jobs_complete;
    protected entity next_job;
    
    public SeleniumGridHub() {
	this("SeleniumGridHub", 3, 10);
    }
    
    public SeleniumGridHub(String name, int Number_nodes, int Number_jobs) {
	super(name);
	addInport("code");
	addInport("status0");
	addInport("status1");
	addInport("status2");
	addOutport("out0");
	addOutport("out1");
	addOutport("out2");
	// for (int i=0; i<number_nodes; i++){
	//     addInport("status"+Integer.toString(i));
	//     addOutport("out"+Integer.toString(i));
	// }
	addOutport("suite-status");
	number_nodes = Number_nodes;
	number_jobs = Number_jobs;
	addTestInput("status1", new entity("free"));
	addTestInput("status1", new entity("free"), 20);
    }

    public void initialize() {
	phase = "passive";
	sigma = INFINITY;
	jobs_queue = new Queue();
	node_ready = 1;
	jobs_complete = 0;
	for (int i=0; i<number_jobs; i++){
	    entity job = new entity("job"+Integer.toString(i));
	    jobs_queue.add(job);
	}
	super.initialize();
    }

    public void deltext(double e, message x) {
	Continue(e);

	for (int i=0; i<x.getLength(); i++) {
	    for (int j=0; j<number_nodes; j++)
		if (messageOnPort(x, "status"+Integer.toString(j), i)) {
		    node_ready = j;
		    jobs_complete += 1;
		    if (jobs_complete == number_jobs) {
			holdIn("done", 0);
		    } else {
			holdIn("transmitting", 0);
		    }
		}
	    if (messageOnPort(x, "code", i))
		holdIn("initials", 0);
	}
    }

    
    public void deltint() {
	passivate();
    }
    
    public void deltcon(double e, message x) {
	System.out.println("confluent");
	deltint();
	deltext(0, x);
    }
    
    public message out() {
	message m = new message();
	if (phaseIs("initials")){
	    for (int i=0; i<number_nodes; i++){
		if (jobs_queue.size() > 0) {
		    next_job = (entity)jobs_queue.remove();
		    m.add(makeContent("out"+Integer.toString(i), next_job));
		}
	    }
	} else if (phaseIs("transmitting")){
	    if (jobs_queue.size() > 0) {
		next_job = (entity)jobs_queue.remove();
		m.add(makeContent("out"+Integer.toString(node_ready), next_job));
	    }
	} else if (phaseIs("done")){
	    entity completion = new entity("Done");
	    m.add(makeContent("suite-status", completion));
	}
	return m;
    }
    
    public void showState() {
	super.showState();
	// System.out.println("job: " + job.getName());
    }
    
    public String getTooltipText() {
	return super.getTooltipText();
    }
}