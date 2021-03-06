import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import NotFound from './pages/404';
import Invitation from './pages/Invitation';
import ChairmanMessage from './pages/ChairmanMessage';
import DirectorMessage from './pages/DirectorMessage';
import Brochure from './pages/Brochure';
import WhyRecruit from './pages/WhyRecruit';
import PlacementStatistics from './pages/PlacementStatistics';
import PlacementProcedure from './pages/PlacementProcedure';
import RecruiterGuidelines from './pages/RecruiterGuidelines';
import PastRecruiters from './pages/PastRecruiters';
import AIPCNorms from './pages/AIPCNorms';
import Achievements from './pages/Achievements';
import Prospective from './pages/Prospective';
import StudentGuidelines from './pages/StudentGuidelines';
import Internships from './pages/Internships';
import JAF from './pages/JAF';
import IAF from './pages/IAF';
import ContactUs from './pages/ContactUs';
import ReachUs from './pages/ReachUs';
import PlacementTeam from './pages/PlacementTeam';
import CareerCounselling from './pages/CareerCounselling';
import StudentLogin from './pages/StudentLogin';
import RecruiterLogin from './pages/RecruiterLogin';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/Invitation" component={Invitation} />
        <Route path="/ChairmanMessage" component={ChairmanMessage} />
        <Route path="/DirectorMessage" component={DirectorMessage} />
        <Route path="/WhyRecruit" component={WhyRecruit} />
        <Route path="/Brochure" component={Brochure} />
        <Route path="/PlacementStatistics" component={PlacementStatistics} />
        <Route path="/PlacementProcedure" component={PlacementProcedure} />
        <Route path="/RecruiterGuidelines" component={RecruiterGuidelines} />
        <Route path="/PastRecruiters" component={PastRecruiters} />
        <Route path="/AIPCNorms" component={AIPCNorms} />
        <Route path="/Achievements" component={Achievements} />
        <Route path="/Prospective" component={Prospective} />
        <Route path="/StudentGuidelines" component={StudentGuidelines} />
        <Route path="/Internships" component={Internships} />
        <Route path="/JAF" component={JAF} />
        <Route path="/IAF" component={IAF} />
        <Route path="/ContactUs" component={ContactUs} />
        <Route path="/ReachUs" component={ReachUs} />
        <Route path="/PlacementTeam" component={PlacementTeam} />
        <Route path="/CareerCounselling" component={CareerCounselling} />
        <Route path="/StudentLogin" component={StudentLogin} />
        <Route path="/RecruiterLogin" component={RecruiterLogin} />
        <Route default component={NotFound} />
      </Switch>
    </Router>
  );
}

export default App;
