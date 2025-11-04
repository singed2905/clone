import json
import os
from typing import Dict, List, Optional, Any

class ConfigLoader:
    """Configuration loader for ConvertKeylogApp v2.2
    
    Handles loading configuration from JSON files with fallback mechanisms.
    """
    
    def __init__(self):
        self.base_config_path = "config"
        self.modes_config_file = "modes.json"
        self._cached_modes = None
        
    def get_available_modes(self) -> List[str]:
        """Get list of available mode names from configuration
        
        Returns:
            List of mode names like ['Equation Mode', 'Polynomial Mode', 'Geometry Mode', 'Vector Mode']
        """
        if self._cached_modes is not None:
            return self._cached_modes
            
        try:
            modes_path = os.path.join(self.base_config_path, self.modes_config_file)
            
            if not os.path.exists(modes_path):
                # Fallback to default modes if config file doesn't exist
                self._cached_modes = ["Equation Mode", "Polynomial Mode", "Geometry Mode", "Vector Mode"]
                return self._cached_modes
                
            with open(modes_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                
            modes_data = config_data.get('modes', {})
            display_order = config_data.get('display_order', [])
            
            # Build mode names list based on display order
            mode_names = []
            for mode_key in display_order:
                if mode_key in modes_data and modes_data[mode_key].get('enabled', True):
                    mode_names.append(modes_data[mode_key]['name'])
                    
            # Add any enabled modes not in display order
            for mode_key, mode_config in modes_data.items():
                if mode_config.get('enabled', True) and mode_config['name'] not in mode_names:
                    mode_names.append(mode_config['name'])
                    
            self._cached_modes = mode_names if mode_names else ["Equation Mode", "Polynomial Mode", "Geometry Mode", "Vector Mode"]
            return self._cached_modes
            
        except Exception as e:
            print(f"Warning: Failed to load modes configuration: {e}")
            # Return default modes on any error
            self._cached_modes = ["Equation Mode", "Polynomial Mode", "Geometry Mode", "Vector Mode"]
            return self._cached_modes
    
    def get_mode_config(self, mode_name: str) -> Optional[Dict[str, Any]]:
        """Get configuration for a specific mode
        
        Args:
            mode_name: Name of the mode (e.g., 'Equation Mode')
            
        Returns:
            Dictionary containing mode configuration or None if not found
        """
        try:
            modes_path = os.path.join(self.base_config_path, self.modes_config_file)
            
            if not os.path.exists(modes_path):
                print(f"Warning: Config file {modes_path} not found")
                return None
                
            with open(modes_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                
            modes_data = config_data.get('modes', {})
            
            # Find mode by name
            for mode_key, mode_config in modes_data.items():
                if mode_config.get('name') == mode_name:
                    return mode_config
                    
            print(f"Warning: Mode '{mode_name}' not found in configuration")
            return None
            
        except Exception as e:
            print(f"Error loading mode config for '{mode_name}': {e}")
            return None
    
    def get_mode_specific_config(self, mode_name: str, config_filename: str) -> Optional[Dict[str, Any]]:
        """Load mode-specific configuration file
        
        Args:
            mode_name: Name of the mode
            config_filename: Name of the configuration file to load
            
        Returns:
            Dictionary containing configuration data or None if not found
        """
        try:
            # Get mode config to find config path
            mode_config = self.get_mode_config(mode_name)
            if not mode_config:
                return None
                
            config_path = mode_config.get('config_path', '')
            if not config_path:
                return None
                
            full_path = os.path.join(config_path, config_filename)
            
            if not os.path.exists(full_path):
                print(f"Warning: Config file {full_path} not found")
                return None
                
            with open(full_path, 'r', encoding='utf-8') as f:
                return json.load(f)
                
        except Exception as e:
            print(f"Error loading mode-specific config '{config_filename}' for '{mode_name}': {e}")
            return None
    
    def reload_config(self):
        """Reload configuration from files (clears cache)"""
        self._cached_modes = None
        
    def get_app_metadata(self) -> Dict[str, Any]:
        """Get application metadata from configuration
        
        Returns:
            Dictionary containing app metadata
        """
        try:
            modes_path = os.path.join(self.base_config_path, self.modes_config_file)
            
            if not os.path.exists(modes_path):
                return {
                    "version": "2.2",
                    "total_modes": 4,
                    "description": "ConvertKeylogApp - Math to Keylog Converter"
                }
                
            with open(modes_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                
            return config_data.get('metadata', {
                "version": "2.2",
                "total_modes": 4,
                "description": "ConvertKeylogApp - Math to Keylog Converter"
            })
            
        except Exception as e:
            print(f"Error loading app metadata: {e}")
            return {
                "version": "2.2",
                "total_modes": 4,
                "description": "ConvertKeylogApp - Math to Keylog Converter"
            }

# Global instance
config_loader = ConfigLoader()
