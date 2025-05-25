import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Page Config
st.set_page_config(
    page_title="🚀 Rocket Launch Center",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .launch-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #e74c3c 0%, #c0392b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .page-intro {
        font-size: 1.2rem;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: linear-gradient(135deg, #ffe8e8 0%, #ffcccb 100%);
        border-radius: 15px;
        border-left: 5px solid #e74c3c;
    }
    .countdown-card {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 12px 40px rgba(231, 76, 60, 0.3);
    }
    .mission-card {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(52, 152, 219, 0.2);
    }
    .rocket-card {
        background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
        padding: 1.2rem;
        border-radius: 12px;
        color: white;
        margin: 0.8rem 0;
        text-align: center;
    }
    .launch-stat {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .agency-badge {
        display: inline-block;
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        margin: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

class LaunchTracker:
    def __init__(self):
        self.spacex_upcoming_url = "https://api.spacexdata.com/v4/launches/upcoming"
        self.spacex_past_url = "https://api.spacexdata.com/v4/launches/past"
        self.spacex_rockets_url = "https://api.spacexdata.com/v4/rockets"
        self.spacex_launchpads_url = "https://api.spacexdata.com/v4/launchpads"
        
    def get_upcoming_launches(self, limit=10):
        """Holt kommende SpaceX Starts"""
        try:
            response = requests.get(f"{self.spacex_upcoming_url}?limit={limit}", timeout=15)
            response.raise_for_status()
            
            data = response.json()
            
            # Nur zukünftige Launches filtern
            now = datetime.now()
            future_launches = []
            
            for launch in data:
                if launch.get('date_utc'):
                    try:
                        launch_date = datetime.fromisoformat(launch['date_utc'].replace('Z', '+00:00'))
                        if launch_date.replace(tzinfo=None) > now:
                            future_launches.append(launch)
                    except:
                        continue
            
            return sorted(future_launches, key=lambda x: x.get('date_utc', ''))[:limit]
            
        except Exception as e:
            st.warning(f"⚠️ SpaceX API temporarily unavailable")
            return self._get_simulated_launches()
    
    def get_recent_launches(self, limit=5):
        """Holt kürzliche SpaceX Starts"""
        try:
            response = requests.get(f"{self.spacex_past_url}?limit={limit}", timeout=15)
            response.raise_for_status()
            
            data = response.json()
            return sorted(data, key=lambda x: x.get('date_utc', ''), reverse=True)[:limit]
            
        except Exception as e:
            return []
    
    def get_rocket_info(self, rocket_id):
        """Holt Raketen-Informationen"""
        try:
            response = requests.get(f"{self.spacex_rockets_url}/{rocket_id}", timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except Exception as e:
            return None
    
    def get_launchpad_info(self, launchpad_id):
        """Holt Startplatz-Informationen"""
        try:
            response = requests.get(f"{self.spacex_launchpads_url}/{launchpad_id}", timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except Exception as e:
            return None
    
    def calculate_launch_stats(self, launches):
        """Berechnet Launch-Statistiken"""
        if not launches:
            return {}
        
        successful = len([l for l in launches if l.get('success') == True])
        failed = len([l for l in launches if l.get('success') == False])
        pending = len([l for l in launches if l.get('success') is None])
        
        return {
            'total': len(launches),
            'successful': successful,
            'failed': failed,
            'pending': pending,
            'success_rate': (successful / (successful + failed) * 100) if (successful + failed) > 0 else 0
        }
    
    def _get_simulated_launches(self):
        """Fallback für simulierte Launches"""
        base_time = datetime.now()
        
        return [
            {
                'name': 'Starlink Group 8-7',
                'date_utc': (base_time + timedelta(days=3)).isoformat() + 'Z',
                'details': 'Deployment of 23 Starlink satellites to low Earth orbit.',
                'rocket': 'falcon9',
                'launchpad': 'ksc_lc_39a',
                'success': None
            },
            {
                'name': 'Crew-9 Mission',
                'date_utc': (base_time + timedelta(days=12)).isoformat() + 'Z',
                'details': 'NASA Commercial Crew mission to the International Space Station.',
                'rocket': 'falcon9',
                'launchpad': 'ksc_lc_39a',
                'success': None
            }
        ]

def format_countdown(launch_date_str):
    """Formatiert Countdown bis zum Launch"""
    try:
        launch_date = datetime.fromisoformat(launch_date_str.replace('Z', '+00:00'))
        now = datetime.now(launch_date.tzinfo)
        
        if launch_date > now:
            delta = launch_date - now
            days = delta.days
            hours, remainder = divmod(delta.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            
            return {
                'countdown': f"{days}d {hours}h {minutes}m",
                'days': days,
                'hours': hours,
                'minutes': minutes,
                'status': 'upcoming'
            }
        else:
            return {
                'countdown': 'Recently Launched',
                'days': 0,
                'hours': 0,
                'minutes': 0,
                'status': 'past'
            }
    except:
        return {
            'countdown': 'TBD',
            'days': 0,
            'hours': 0,
            'minutes': 0,
            'status': 'unknown'
        }

def create_launch_timeline(launches):
    """Erstellt Launch Timeline Visualization"""
    if not launches:
        return None
    
    # Prepare data for timeline
    timeline_data = []
    
    for launch in launches[:10]:  # Top 10 launches
        launch_date = launch.get('date_utc', '')
        if launch_date:
            try:
                dt = datetime.fromisoformat(launch_date.replace('Z', '+00:00'))
                timeline_data.append({
                    'Mission': launch.get('name', 'Unknown'),
                    'Date': dt,
                    'Agency': 'SpaceX',
                    'Status': 'Upcoming' if launch.get('success') is None else ('Success' if launch.get('success') else 'Failed'),
                    'Rocket': launch.get('rocket', 'Unknown')
                })
            except:
                continue
    
    if not timeline_data:
        return None
    
    df = pd.DataFrame(timeline_data)
    
    # Create timeline plot
    fig = px.scatter(
        df, 
        x='Date', 
        y='Mission',
        color='Status',
        size_max=15,
        title='🚀 Upcoming SpaceX Launch Timeline',
        color_discrete_map={
            'Upcoming': '#3498db',
            'Success': '#27ae60',
            'Failed': '#e74c3c'
        }
    )
    
    fig.update_layout(
        height=500,
        template='plotly_white',
        xaxis_title='Launch Date',
        yaxis_title='Mission',
        showlegend=True
    )
    
    return fig

def main():
    # Header
    st.markdown('<h1 class="launch-header">🚀 ROCKET LAUNCH CENTER</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-intro">
        <strong>🌍 Global Space Launch Tracking & Analysis</strong><br><br>
        Monitor upcoming rocket launches from SpaceX and track mission success rates. 
        From Starlink deployments to crew missions - never miss a launch! 
        SpaceX has revolutionized space access with reusable rockets! 🔥
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize Launch Tracker
    launcher = LaunchTracker()
    
    # Sidebar Controls
    st.sidebar.markdown("## 🎛️ Launch Control Center")
    
    auto_refresh = st.sidebar.checkbox("🔄 Auto-Refresh (60s)", value=False)
    if auto_refresh:
        time.sleep(60)
        st.rerun()
    
    if st.sidebar.button("🚀 Update Launch Data", type="primary"):
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🚀 Launch Quick Facts")
    st.sidebar.markdown("""
    - **SpaceX Falcon 9:** Most flown rocket
    - **Reusability:** Boosters land & refly
    - **Starlink:** ~5,000 satellites deployed
    - **Crew Dragon:** NASA astronaut transport
    - **Success Rate:** >95% recent missions
    - **Launch Cadence:** ~100 launches/year
    - **Turnaround:** As fast as 2 weeks
    """)
    
    # Get Launch Data
    with st.spinner("🚀 Contacting Launch Control..."):
        upcoming_launches = launcher.get_upcoming_launches(10)
        recent_launches = launcher.get_recent_launches(5)
        
        # Next Launch Countdown (Featured)
        if upcoming_launches:
            next_launch = upcoming_launches[0]
            countdown_info = format_countdown(next_launch.get('date_utc', ''))
            
            st.markdown("### 🎯 Next SpaceX Launch")
            
            col_countdown, col_details = st.columns([1, 1])
            
            with col_countdown:
                st.markdown(f"""
                <div class="countdown-card">
                    <h2>🚀 {next_launch.get('name', 'Mission')}</h2>
                    <h1 style="font-size: 3rem; margin: 1rem 0;">{countdown_info['countdown']}</h1>
                    <p style="font-size: 1.2rem;">T-minus countdown</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_details:
                launch_date = next_launch.get('date_utc', '')
                formatted_date = 'TBD'
                if launch_date:
                    try:
                        dt = datetime.fromisoformat(launch_date.replace('Z', '+00:00'))
                        formatted_date = dt.strftime('%d.%m.%Y %H:%M UTC')
                    except:
                        pass
                
                details = next_launch.get('details') or 'Mission details coming soon'
                details_text = str(details)[:150] + ('...' if len(str(details)) > 150 else '')
                
                st.markdown(f"""
                <div class="mission-card">
                    <h3>🛸 Mission Details</h3>
                    <p><strong>📅 Launch Date:</strong> {formatted_date}</p>
                    <p><strong>🚀 Vehicle:</strong> Falcon 9</p>
                    <p><strong>📍 Location:</strong> Kennedy Space Center</p>
                    <p><strong>📊 Details:</strong> {details_text}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Launch Statistics
        st.markdown("---")
        st.markdown("### 📊 Launch Performance Analytics")
        
        all_launches = upcoming_launches + recent_launches
        stats = launcher.calculate_launch_stats(recent_launches)  # Only calculate from recent launches
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="launch-stat">
                <h3>🚀 Upcoming</h3>
                <h2>{len(upcoming_launches)}</h2>
                <p>Scheduled Launches</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="launch-stat">
                <h3>✅ Successful</h3>
                <h2>{stats.get('successful', 0)}</h2>
                <p>Recent Missions</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="launch-stat">
                <h3>📈 Success Rate</h3>
                <h2>{stats.get('success_rate', 0):.1f}%</h2>
                <p>Mission Success</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="launch-stat">
                <h3>🎯 Total</h3>
                <h2>{stats.get('total', 0)}</h2>
                <p>Recent Launches</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Launch Timeline Visualization
        if upcoming_launches:
            st.markdown("---")
            st.markdown("### 📅 Launch Timeline")
            
            timeline_fig = create_launch_timeline(upcoming_launches)
            if timeline_fig:
                st.plotly_chart(timeline_fig, use_container_width=True)
        
        # Upcoming Launches List
        st.markdown("---")
        st.markdown("### 🗓️ Upcoming Launch Schedule")
        
        if upcoming_launches:
            for i, launch in enumerate(upcoming_launches[:5]):
                countdown_info = format_countdown(launch.get('date_utc', ''))
                
                launch_date = launch.get('date_utc', '')
                formatted_date = 'TBD'
                if launch_date:
                    try:
                        dt = datetime.fromisoformat(launch_date.replace('Z', '+00:00'))
                        formatted_date = dt.strftime('%d.%m.%Y %H:%M UTC')
                    except:
                        pass
                
                details = launch.get('details') or 'Mission details to be announced'
                details_text = str(details)[:100] + ('...' if len(str(details)) > 100 else '')
                
                st.markdown(f"""
                <div class="rocket-card">
                    <h4>🚀 {launch.get('name', 'Mission')} | {countdown_info['countdown']}</h4>
                    <p><strong>📅 Date:</strong> {formatted_date} | <strong>🎯 Status:</strong> Scheduled</p>
                    <p>{details_text}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("🚀 No upcoming launches currently scheduled. Check back soon!")
        
        # Recent Launches
        if recent_launches:
            st.markdown("---")
            st.markdown("### 📈 Recent Launch History")
            
            for launch in recent_launches[:3]:
                success_icon = "✅" if launch.get('success') == True else "❌" if launch.get('success') == False else "⏳"
                success_text = "Success" if launch.get('success') == True else "Failed" if launch.get('success') == False else "Pending"
                
                launch_date = launch.get('date_utc', '')
                formatted_date = 'Unknown'
                if launch_date:
                    try:
                        dt = datetime.fromisoformat(launch_date.replace('Z', '+00:00'))
                        formatted_date = dt.strftime('%d.%m.%Y')
                    except:
                        pass
                
                details = launch.get('details') or 'Successful mission completion'
                details_text = str(details)[:100] + ('...' if len(str(details)) > 100 else '')
                
                st.markdown(f"""
                <div class="rocket-card" style="background: linear-gradient(135deg, {'#27ae60' if launch.get('success') else '#34495e'} 0%, {'#2ecc71' if launch.get('success') else '#2c3e50'} 100%);">
                    <h4>{success_icon} {launch.get('name', 'Mission')} | {success_text}</h4>
                    <p><strong>📅 Date:</strong> {formatted_date} | <strong>🚀 Vehicle:</strong> Falcon 9</p>
                    <p>{details_text}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
        🚀 <strong>Rocket Launch Center</strong> 🚀<br>
        📡 Real-time launch data from SpaceX and global space agencies<br>
        🌍 Tracking humanity's journey to the stars, one launch at a time
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()