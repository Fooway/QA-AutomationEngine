/*     
 *    
 *  Author     : Neal DeBuhr
 *  Version    : DEVS-Suite 3.0.0  
 *  Date       : 12-27-2017
 */
package CoreOne;
import java.awt.*;

import GenCol.*;

import model.modeling.*;
import model.simulation.*;

import view.modeling.ViewableAtomic;
import view.modeling.ViewableComponent;
import view.modeling.ViewableDigraph;
import view.simView.*;

public class JenkinsOnline extends ViewableDigraph {
    private ViewableDigraph jenkins;
    private ViewableDigraph github;
    private ViewableDigraph empty0;
    private ViewableDigraph empty1;
    private ViewableAtomic email;
    
    public JenkinsOnline(){
	super("JenkinsOnline");
	jenkins = new Jenkins();
	github = new GitHub();
	email = new NealEmail();
	empty0 = new Empty("Empty0", "repo-request");
	empty1 = new Empty("Empty1", "repository");

	add(jenkins);
	add(github);
	add(email);
	add(empty0);
	add(empty1);

	addInports();
	addOutports();
	addCouplings();
    }

    private void addInports(){
    }
    
    private void addOutports(){
    }
   
    private void addCouplings(){
	addCoupling(jenkins, "coord-github-request", empty0, "0-in");
	addCoupling(jenkins, "job0-github-request", empty0, "1-in");
	addCoupling(jenkins, "job1-github-request", empty0, "2-in");
	addCoupling(jenkins, "job2-github-request", empty0, "3-in");
	addCoupling(jenkins, "job3-github-request", empty0, "4-in");
	addCoupling(jenkins, "job4-github-request", empty0, "5-in");

	addCoupling(empty0, "0-out", github, "0-in");
	addCoupling(empty0, "1-out", github, "1-in");
	addCoupling(empty0, "2-out", github, "2-in");
	addCoupling(empty0, "3-out", github, "3-in");
	addCoupling(empty0, "4-out", github, "4-in");
	addCoupling(empty0, "5-out", github, "5-in");

	addCoupling(github, "0-out", empty1, "0-in");
	addCoupling(github, "1-out", empty1, "1-in");
	addCoupling(github, "2-out", empty1, "2-in");
	addCoupling(github, "3-out", empty1, "3-in");
	addCoupling(github, "4-out", empty1, "4-in");
	addCoupling(github, "5-out", empty1, "5-in");

	addCoupling(empty1, "0-out", jenkins, "coord-github-response");
	addCoupling(empty1, "1-out", jenkins, "job0-github-response");
	addCoupling(empty1, "2-out", jenkins, "job1-github-response");
	addCoupling(empty1, "3-out", jenkins, "job2-github-response");
	addCoupling(empty1, "4-out", jenkins, "job3-github-response");
	addCoupling(empty1, "5-out", jenkins, "job4-github-response");

	addCoupling(jenkins, "results", email, "in");

	
    }

    /**
     * Automatically generated by the SimView program.
     * Do not edit this manually, as such changes will get overwritten.
     */
    public void layoutForSimView()
    {
        preferredSize = new Dimension(1670, 862);
        ((ViewableComponent)withName("Empty1")).setPreferredLocation(new Point(85, 244));
        ((ViewableComponent)withName("Empty0")).setPreferredLocation(new Point(1096, 241));
        ((ViewableComponent)withName("Jenkins")).setPreferredLocation(new Point(162, 375));
        ((ViewableComponent)withName("GitHub")).setPreferredLocation(new Point(487, 199));
        ((ViewableComponent)withName("NealEmail")).setPreferredLocation(new Point(1116, 758));
    }
}
