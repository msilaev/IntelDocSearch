import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';

const App: React.FC = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" component={HomePage} />
            </Switch>
        </Router>
    );
};

export default App;